from django.contrib import admin
from .models import ProductCategory
from .models import Product
from .models import Nutrient
from .models import ProductNutrient
from .models import ProductTag

# Register your models here.
admin.site.register(Nutrient)
admin.site.register(ProductNutrient)
admin.site.register(ProductTag)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'si_unit',
                    'p_unit', 'is_active', 'unit_quantity',
                    'price', 'stock', 'on_promotion',
                    'slug']
    list_filter = ['is_active']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields = {'slug': ('name',)}