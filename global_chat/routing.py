from django.urls import path
from .consumers import GlobalChatConsumer

websocket_urlpatterns = [
    path('ws/global-chat/', GlobalChatConsumer.as_asgi()),
]
