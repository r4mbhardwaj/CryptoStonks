from django.urls import path
from .views import price_chart, coin_list

urlpatterns = [
    path('', coin_list, name='coin_list'),
    path('price_chart/<str:symbol>/', price_chart, name='price_chart'),
]