from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Products


class OrderForm(forms.Form):
    order_data = forms.CharField(widget=forms.HiddenInput())

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact', 'credits', 'total_spent']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['Name', 'Price', 'Category']