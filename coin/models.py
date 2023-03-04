from django.db import models
import requests


class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def fetch_price(self):
        # USDT is the stablecoin that Binance uses as a trading pair
        symbol = f"{self.symbol}USDT"
        api_url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(api_url)
        response_json = response.json()
        if "price" in response_json:
            price_usd = float(response_json["price"])
            return price_usd
        else:
            print(f"Error fetching price for {self.name}")
            print(response_json)
            return None


class Price(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    price_usd = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.coin.name}: ${self.price_usd:.2f}'
