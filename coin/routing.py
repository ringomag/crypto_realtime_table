from django.urls import path
from .consumers import WSCoinConsumer

ws_urlpatterns = [
    path('ws/coin/', WSCoinConsumer.as_asgi())
    ]