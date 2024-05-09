from django.views.generic import TemplateView


class StockItems(TemplateView):
    template_name = 'stock_items/stock_items.html'
