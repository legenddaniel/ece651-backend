from django.contrib import admin
from .models import ProductsCategory
from .models import Product
from .models import Nutrient
from .models import ProductNutrient
from .models import ProductTag

# Register your models here.
admin.site.register(ProductsCategory)
admin.site.register(Product)
admin.site.register(Nutrient)
admin.site.register(ProductNutrient)
admin.site.register(ProductTag)