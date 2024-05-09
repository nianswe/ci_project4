from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stock_items(request):
    return HttpResponse("Hello there! StockItems")
