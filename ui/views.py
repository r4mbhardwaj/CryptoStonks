from django.shortcuts import render
from coin.models import Coin

def coin_list(request):
    coins = Coin.objects.all()
    return render(request, 'ui/coin_list.html', {'coins': coins})

def price_chart(request, symbol):
    return render(request, 'ui/price_chart.html', {'symbol': symbol})
