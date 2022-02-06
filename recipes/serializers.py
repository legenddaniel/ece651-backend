from rest_framework import serializers
from .models import Recipe
from products.models import Product

class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','image_url', 'price']

class RecipeProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients_product = serializers.SerializerMethodField()

    def get_ingredients_product(self, obj):
        selected_products = Product.objects.filter(
            recipe_products__name=obj).all()
        return RecipeProductSerializer(selected_products, many=True).data

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'image_url', 'cuisine', 'products', 'ingredients_product', 'rating', 'total_views']