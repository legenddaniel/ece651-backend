from rest_framework import serializers

from .models import Order, OrderItem
from products.serializers import ProductDetailSerializer
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
