from django.contrib import admin
from .models import Category
from .models import Stock_Item
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Stock_Item)

@admin.register(Stock_Item)
class StockItemAdmin(SummernoteModelAdmin):

    list_display = ('item_name', 'slug', 'brands')
    search_fields = ['item_name', 'product_name', 'category_name', 'brands']
    list_filter = ('item_name',)
    prepopulated_fields = {'slug': ('item_name',)}
    
    
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('category_name', 'slug', 'category_description')
    search_fields = ['category_name', 'category_description']
    list_filter = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}

