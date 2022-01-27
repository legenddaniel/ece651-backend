from rest_framework import serializers
from .models import Products
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        # fields = '__all__'
        fields = ['products_id', 'name', 'description', 'image', 'price']