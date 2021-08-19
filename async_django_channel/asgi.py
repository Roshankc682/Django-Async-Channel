import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from async_django_channel.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_django_channel.settings')

application = get_asgi_application()


# first protocol and then routers
application = get_asgi_application()

ws_patterns = [
    path('ws/firstchannel/',TestConsumer),
    path('ws/async/',NewClass),
    
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
