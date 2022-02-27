from rest_framework import serializers

from .models import CartItem
from products.serializers import ProductDetailSerializer
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(many=False, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Product.objects.all(), source='product')

    class Meta:
        model = CartItem
        fields = '__all__'

    def create(self, validated_data):
        cart_items = CartItem.objects.filter(user_id=validated_data['user'])
        for item in cart_items:
            if item.product.id == validated_data['product'].id:
                item.quantity = item.quantity + validated_data['quantity']
                item.save()
                return True

        item = CartItem.objects.create(**validated_data)
        item.save()

        return item
