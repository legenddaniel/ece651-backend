from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': True},
            'product': {'required': True},
            'quantity': {'required': True},
        }
