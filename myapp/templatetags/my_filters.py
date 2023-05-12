from django import template
from ..models import Products

register = template.Library()

@register.filter
def get_item(dictionary, key):
    product = Products.objects.get(id=key)
    return product
