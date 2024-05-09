"""
URL configuration for stockhandler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stock_items.views import stock_items
from home.views import homepage
from shopping_list.views import shopping_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name='home'),
    path('stock_items/', stock_items, name='stock_items'),
    path('shopping_list/', shopping_list, name='shopping_list'),

]