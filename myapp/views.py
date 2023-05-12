from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum, Count
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, TruncQuarter
from .models import Order, Products, OrderReminder, Customer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
import json, uuid
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CustomerForm, ProductForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def home(request):
    return render(request, 'home.html')

def tables(request, table_id=None):
    if table_id:
        request.session['table_id'] = table_id
        return redirect('menu')
    
    orders = Order.objects.filter(is_checkout=False)  # 从订单数据库中获取未结账的订单信息
    tables = [f"{i:02d}" for i in range(1, 21)]
    context = {'tables': tables, 'orders': orders}  # 将tables和orders放在同一个字典中
    return render(request, 'table.html', context)


def menu(request, table_id):
    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    order_number = f"{today_str} {str(uuid.uuid4().int)[:10]} {str(table_id)}"
    
    categories = Products.objects.values_list('Category', flat=True).distinct()
    
    category = request.GET.get('category', 'all')
    if category != 'all':
        products_list = Products.objects.filter(Category=category)
    else:
        products_list = Products.objects.all()
    
    context = {
        'menu_items': products_list,
        'table_id': table_id,
        'order_number': order_number,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def update_order(request, table_id):
    if request.method == 'POST':
        shopping_cart = json.loads(request.POST.get('shopping_cart', '{}'))

        request.session[f'shopping_cart_{table_id}'] = shopping_cart
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def your_order_page(request, table_id):
    shopping_cart = request.session.get(f'shopping_cart_{table_id}', {})
    products = {}
    total_price = 0
    order_number = ""  # Initialize the order_number variable
    for product_id, quantity in shopping_cart.items():
        try:
            product = Products.objects.get(ProductsID=product_id)
            total_price += product.Price * quantity
            products[product] = quantity
        except ObjectDoesNotExist:
            pass

        shopping_cart = request.session.get(f'shopping_cart_{table_id}', {})
        order_number = list(shopping_cart.values())[0]['order_number']  

    return render(request, 'order.html', {'products': products, 'total_price': total_price, 'order_number': order_number})

def orders(request):
    unfinished_orders = Order.objects.filter(is_checkout=False).order_by('-created_at')
    context = {
        'orders': unfinished_orders,
    }
    return render(request, 'orders.html', context)

def completed_orders(request):
    unfinished_orders = Order.objects.filter(is_checkout=True)
    context = {
        'orders': unfinished_orders,
    }
    return render(request, 'orders.html', context)

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        table_id = data.get('table_id')
        items = data.get('items')
        order_number = data.get('order_number')
        total_price = data.get('total_price')

        order = Order(table_id=table_id, items=items, order_number=order_number, total_price=total_price)
        order.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def update_order_status(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_checkout = not order.is_checkout
    order.save()
    return redirect('orders')

def checkout_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            order.is_checkout = True
            order.save()
            return JsonResponse({'status': 'success'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})

def kitchen(request):
    unprepared_orders = Order.objects.filter(is_prepared=False).order_by('created_at')
    reminded_orders = Order.objects.filter(is_reminder=True, is_prepared=False).order_by('-created_at')
    for order_obj in unprepared_orders:
        order_obj.created_at = timezone.localtime(order_obj.created_at)
    context = {
        'orders': unprepared_orders,
        'reminded_orders': reminded_orders,
    }
    return render(request, 'kitchen.html', context)

def completed_kitchen(request):
    uncomplete_orders = Order.objects.filter(is_prepared=True).order_by('-created_at')
    context = {
        'orders': uncomplete_orders
    }
    return render(request, 'kitchen.html', context)

def prepare_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_prepared = True
    order.is_reminder = False  # set is_reminder to False
    order.save()
    return redirect('kitchen')

def daily_summary(request):
    daily_orders = Order.objects.filter(is_checkout=True).annotate(day=TruncDay('order_date')).values('day').annotate(order_count=Count('id'), total_revenue=Sum('total_price')).order_by('day')
    weekly_orders = Order.objects.filter(is_checkout=True).annotate(week=TruncWeek('order_date')).values('week').annotate(order_count=Count('id'), total_revenue=Sum('total_price')).order_by('week')
    monthly_orders = Order.objects.filter(is_checkout=True).annotate(month=TruncMonth('order_date')).values('month').annotate(order_count=Count('id'), total_revenue=Sum('total_price')).order_by('month')
    quarterly_orders = Order.objects.filter(is_checkout=True).annotate(quarter=TruncQuarter('order_date')).values('quarter').annotate(order_count=Count('id'), total_revenue=Sum('total_price')).order_by('quarter')

    context = {
        'daily_orders': daily_orders,
        'weekly_orders': weekly_orders,
        'monthly_orders': monthly_orders,
        'quarterly_orders': quarterly_orders,
    }
    return render(request, 'summary.html', context)

def order_remind(request):
    reminder_orders = Order.objects.filter(is_prepared=False, is_reminder=False)
    context = {'reminder_orders': reminder_orders}
    return render(request, 'order_remind.html', context)

@csrf_exempt
def send_order_reminder(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            order.is_reminder = True  # 将 is_reminder 设置为 True
            order.save()
            reminder = OrderReminder(order=order)
            reminder.save()
            return JsonResponse({'status': 'success'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})

def customer_list(request):
    customers = Customer.objects.all()  # 获取所有的客户
    return render(request, 'customer.html', {'customers': customers})  # 渲染模板，并传递客户列表

def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})

def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_edit.html', {'form': form})

def customer_remove(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.delete()
    return redirect('customer_list')

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')  # 修改这里以匹配你的URL配置
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})

def product_list(request):
    query_category = request.GET.get('category')
    query_name = request.GET.get('name')

    products = Products.objects.all()

    if query_category:
        products = products.filter(Category=query_category)

    if query_name:
        products = products.filter(Name__icontains=query_name)

    categories = Products.objects.values_list('Category', flat=True).distinct()
    context = {
        'products': products,
        'categories': categories,
        'selected_category': query_category,
        'search_name': query_name,
    }
    return render(request, 'product.html', context)

def product_edit(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form, 'product': product})

def product_remove(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    return redirect('product_list')
