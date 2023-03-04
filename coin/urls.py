from django.urls import path
from .views import CoinList, CoinDetail, PriceList, PriceDetail

urlpatterns = [
    path('coins/', CoinList.as_view(), name='coin-list'),
    path('coins/<str:symbol>/', CoinDetail.as_view(), name='coin-detail'),
    path('coins/<str:symbol>/prices/', PriceList.as_view(), name='price-list'),
    path('prices/<int:pk>/', PriceDetail.as_view(), name='price-detail'),
]
