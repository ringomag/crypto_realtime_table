from celery import shared_task
from .models import Coin
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

channel_layer = get_channel_layer()


@shared_task
def get_or_create_coins_in_database():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    coins = []

    for coin in data:
        obj, created = Coin.objects.get_or_create(symbol=coin['symbol'])
        obj.name = coin['name']
        obj.image = coin['image']
        obj.price = coin['current_price']
        obj.symbol = coin['symbol']
        obj.rank = coin['market_cap_rank']

        obj.save()

        coins_data = model_to_dict(obj)
        coins.append(coins_data)

    

    async_to_sync(channel_layer.group_send)("coin", {'type': 'socket_get_coins', 'text':coins})
        