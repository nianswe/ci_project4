from django.views.generic import TemplateView


class ShoppingList(TemplateView):
    template_name = 'shopping_list/shopping_list.html'