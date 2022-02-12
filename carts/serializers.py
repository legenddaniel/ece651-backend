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

    def create(self, validated_data):
        cart_items = CartItem.objects.filter(user=self.context['user'])
        for item in cart_items:
            if item.product.id == validated_data['product'].id:
                item.quantity = item.quantity + validated_data['quantity']
                item.save()
                return True
        
        item = CartItem.objects.create(**validated_data)
        item.save()

        return True
