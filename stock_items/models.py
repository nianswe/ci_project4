from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# Create your models here.

class Category(models.Model):
   # schema for the Category model
   category_name = models.CharField(max_length=50, unique=True, null=False)
   category_description = models.CharField(max_length=50, unique=True, null=False)
   slug = models.SlugField(max_length=50, unique=True)
   created_on = models.DateTimeField(auto_now_add=True)
   category_name_id = models.AutoField(primary_key=True, unique=True, null=False)
         
   def __str__(self):
       # __repr__ to represent itself in the form of a string
       return self.category_name


class Stock_Item(models.Model):
    # schema for the StockItem model
    item_name = models.CharField(max_length=50, unique=True, null=False)
    st_id = models.AutoField(primary_key=True, unique=True, null=False)
    is_picked = models.BooleanField(default=False, null=False)
    product_name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    category_name = models.ManyToManyField(Category)
    # category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brands = models.CharField(max_length=50, unique=False, null=True, blank=True)
    quantity = models.CharField(max_length=50, unique=False, null=True)
    code = models.IntegerField(unique=True, null=True, blank=True)
    ecoscore_score = models.IntegerField(unique=False, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='stockitems/', force_format='WEBP',
        null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       # __repr__ to represent itself in the form of a string
       return self.item_name