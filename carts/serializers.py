from rest_framework import serializers

from .models import CartItem
from products.models import Product


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    # Add related objects to response
    product = CartProductSerializer(
        many=False,
        read_only=True,
    )

    # Since `product` field requires object now so need a new `product_id` field for front end. Not included in response.
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': True},
            'product_id': {'required': True},
            'quantity': {'required': True},
        }
