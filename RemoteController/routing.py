from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/RemoteController/ESP32/', consumers.HomeConsumer.as_asgi()),
]