from django.db import models, transaction
from django.db.models import Max
import datetime
from uuid import uuid4
from decimal import Decimal

class Spicy(models.Model):
    id = models.IntegerField(primary_key=True)
    spicy_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.spicy_name

class Paralysis(models.Model):
    id = models.IntegerField(primary_key=True)
    paralysis_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.paralysis_name
    
class Product(models.Model):
    id = models.UUIDField(default=uuid4, editable=False)
    ProductsID = models.CharField(primary_key=True, max_length=128, unique=True) 
    Name = models.CharField(max_length=128)
    SecondaryName = models.CharField(max_length=128, default='')
    descreption = models.CharField(max_length=5000, default='')  # 添加英文输入字段
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Category = models.CharField(max_length=128)
    spicy = models.ForeignKey(Spicy, on_delete=models.SET_NULL, blank=True, null=True)
    paralysis = models.ForeignKey(Paralysis, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.ProductsID:
            with transaction.atomic():
                # 获取这个Category的当前最大数字
                max_number = Product.objects.filter(Category=self.Category).aggregate(Max('ProductsID'))['ProductsID__max']
                
                if max_number is None:
                    # 如果这是这个Category的第一个产品，就从1开始
                    next_number = 1
                else:
                    # 否则，就增加最大的数字
                    next_number = int(max_number[-4:]) + 1
                
                # 生成新的ProductsID
                self.ProductsID = f"{self.Category}{next_number:04}"
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Name

class Order(models.Model):
    table_id = models.IntegerField()
    items = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    is_checkout = models.BooleanField(default=False)
    is_prepared = models.BooleanField(default=False)
    is_reminder = models.BooleanField(default=False)
    order_number = models.CharField(max_length=255)
    total_price = models.DecimalField(default=Decimal('0'), max_digits=10, decimal_places=2)
    order_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Order {self.order_number} (Table {self.table_id})"

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

class OrderReminder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for Order {self.order.order_number} sent at {self.sent_at}"
    
