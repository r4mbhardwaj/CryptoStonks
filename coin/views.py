from rest_framework import generics
from .models import Coin, Price
from .serializers import CoinSerializer, PriceSerializer


class CoinList(generics.ListCreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class CoinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    lookup_field = 'symbol'


class PriceList(generics.ListCreateAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        symbol = self.kwargs['symbol']
        return Price.objects.filter(coin__symbol=symbol)


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
