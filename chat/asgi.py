import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack


import apps.chats.routing
import apps.global_chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.chats.routing.websocket_urlpatterns
            + apps.global_chat.routing.websocket_urlpatterns
        )
    ),
})
