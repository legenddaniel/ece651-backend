from django.contrib import admin
from .models import Products_Category
from .models import Products
from .models import Nutrients
from .models import Product_Nutrients
from .models import Product_Tag

# Register your models here.
admin.site.register(Products_Category)
admin.site.register(Products)
admin.site.register(Nutrients)
admin.site.register(Product_Nutrients)
admin.site.register(Product_Tag)