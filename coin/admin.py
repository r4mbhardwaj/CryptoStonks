from django.contrib import admin

from .models import Coin, Price

admin.site.register(Coin)
admin.site.register(Price)
