from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from myapp.consumers import KitchenConsumer

websocket_urlpatterns = [
    path('ws/kitchen/', KitchenConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})