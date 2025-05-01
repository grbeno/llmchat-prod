# chat/routing.py

from django.urls import re_path
from .views import ChatConsumer

# Define WebSocket URL patterns for the chat application
websocket_urlpatterns = [
    re_path(r"^ws/chat/$", ChatConsumer.as_asgi(), name="chat"),
]