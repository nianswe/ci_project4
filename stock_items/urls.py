from django.urls import path
from .views import StockItems

urlpatterns =[
    path('', StockItems.as_view(), name='StockItems'),
]