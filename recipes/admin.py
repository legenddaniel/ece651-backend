from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import Recipe, ProductQuantity, Label, Nutrient

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ['name', 'description', 'rating',
                    'cuisine',
                    'instructions', 'last_purchase_made',
                    'total_reviews']
    list_editable = ['cuisine']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductQuantity)
class ProductQuantityAdmin(admin.ModelAdmin):
    list_filter = ('recipe__name',)
    search_fields = ['recipe__name']

@admin.register(Nutrient)
class RecipeAdmin(admin.ModelAdmin):
    # exclude = ('recipe',)
    list_display=['recipe', 'calories', 'total_fat',
                  'saturated_fat', 'cholesterol',
                  'sodium', 'total_fiber', 'protein',
                  'carbohydrates', 'potassium']

admin.site.register(Label)