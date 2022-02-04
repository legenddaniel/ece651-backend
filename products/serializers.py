from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_id', 'name', 'description', 'image', 'price']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'