from rest_framework import serializers

from carts.serializers import CartItemSerializer
from orders.serializers import OrderSerializer

from .models import ShippingAddress, User


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    orders = OrderSerializer(many=True, read_only=True)
    shipping_address = ShippingAddressSerializer(many=False, read_only=True)

    class Meta:
        model = User
        exclude = ['password']
