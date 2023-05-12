"""
ASGI config for RestaurantOrderSystem project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestaurantOrderSystem.settings')

application = get_asgi_application()

from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from myapp.consumers import KitchenConsumer

websocket_urlpatterns = [
    path('ws/kitchen/', KitchenConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
