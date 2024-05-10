# from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import generic
from .models import Category
from .models import Stock_Item


class StockItems(generic.ListView):
    model = Stock_Item
    
class Category(generic.ListView):
    model = Category
    
    
# class StockItems(TemplateView):
#    template_name = 'stock_items/stock_items.html'
