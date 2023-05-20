from django import template
from ..models import Product

register = template.Library()

@register.filter
def get_item(dictionary, key):
    product = Product.objects.get(id=key)
    return product
