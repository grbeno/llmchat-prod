# config/urls.py

from django.contrib import admin
from django.urls import path, re_path
from chat.views import React, ChatConsumer


urlpatterns = [
    path('admin/', admin.site.urls),

    # React
    re_path(r'^.*', React.as_view(), name='frontend'),

    # WebSocket
    path('ws/chat/', ChatConsumer.as_asgi()),
    
]
