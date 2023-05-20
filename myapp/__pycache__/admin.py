from django.contrib import admin
from .models import Product, Order, Customer, Spicy, Paralysis

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Spicy)
admin.site.register(Paralysis)