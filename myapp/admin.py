from django.contrib import admin
from .models import Products, Order, Customer

admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Customer)