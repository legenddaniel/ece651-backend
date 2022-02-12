from django.contrib import admin
from .models import ProductCategory
from .models import Product
from .models import ProductTag

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'si_unit',
                    'unit_quantity', 'is_active',
                    'price', 'stock', 'on_promotion',
                    'slug']
    list_filter = ['is_active']
    list_editable = ['price', 'category', 'si_unit', 'unit_quantity', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductTag)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields = {'slug': ('name',)}