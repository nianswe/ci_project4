from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shopping_list(request):
    return HttpResponse("Hello there! Shopping List Page")