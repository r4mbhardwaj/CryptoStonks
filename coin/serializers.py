from rest_framework import serializers
from .models import Coin, Price

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    coin = CoinSerializer(read_only=True)

    class Meta:
        model = Price
        fields = '__all__'

class PriceSerializerValuesOnly(serializers.ModelSerializer):
    coin = CoinSerializer(read_only=True)

    class Meta:
        model = Price
        fields = ['price_usd', 'last_updated']
