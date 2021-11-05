from django.shortcuts import render
from .models import Coin

def index(request):
    coins = Coin.objects.all()
    return render(request, 'index.html', {'coins':coins})