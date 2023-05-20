from django.urls import path, re_path
from . import views, consumers
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path('home/', views.home, name='home'),  # 将登录页面设置为根路径
    path('tables/', views.tables, name='tables'),
    path('table/<int:table_id>/', views.tables, name='tables_table'),
    path('menu/<str:table_id>/', views.menu, name='menu_table'),
    path('menu', views.menu, name='menu'),
    path('your_order_page/<int:table_id>', views.your_order_page, name='your_order_page'),
    path('orders/', views.orders, name='orders'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('checkout_order/<int:order_id>/', views.checkout_order, name='checkout_order'),
    path('completed_orders/', views.completed_orders, name='completed_orders'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('completed_cooking/', views.completed_orders, name='completed_cooking'),
    path('completed_kitchen/', views.completed_kitchen, name='completed_kitchen'),
    path('prepare_order/<int:order_id>/', views.prepare_order, name='prepare_order'),
    path('daily_summary/', views.daily_summary, name='daily_summary'),
    path('order_reminder/', views.order_remind, name='order_reminder'),
    path('send_order_reminder/<int:order_id>/', views.send_order_reminder, name='send_order_reminder'),
    path('customers/', views.customer_list, name='customer_list'),  # 所有客户的路由
    path('customer/add/', views.customer_add, name='customer_add'),
    path('customer/<uuid:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<uuid:customer_id>/remove/', views.customer_remove, name='customer_remove'),
    path('product/add/', views.product_add, name='product_add'),
    path('products/', views.product_list, name='product_list'),
    path('products/<uuid:product_id>/edit/', views.product_edit, name='product_edit'),
    path('products/<uuid:product_id>/remove/', views.product_remove, name='product_remove'),
    path('product/search/', views.product_list, name='product_search'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('print_order/<int:order_id>/', views.print_order, name='print_order'),
]


