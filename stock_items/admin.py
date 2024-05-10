from django.contrib import admin
from .models import Category
from .models import Stock_Item

# Register your models here.
admin.site.register(Category)
admin.site.register(Stock_Item)
