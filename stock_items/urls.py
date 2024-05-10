from django.urls import path
from . import views
# from .views import StockItems

urlpatterns =[
    path('', views.StockItems.as_view(), name='stock_items'),
    path('categories/', views.Category.as_view(), name='categories'),
    
]