from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CartItemSerializer
from .models import CartItem


class CartItemView(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    # Add one item to cart
    def create(self, request):
        serializer = self.serializer_class(
            data={**request.data, 'user': request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(self.get_queryset().values())

    # Update one cart item (e.g. quantity). Do deletion if quantity goes 0.
    def partial_update(self, request, cart_item=None):
        items = CartItem.objects.filter(user=request.user, id=cart_item)
        if not items.count():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        items.update(**request.data)

        return Response(self.get_queryset().values())

    # Clear cart for current user
    def destroy(self, request):
        self.get_queryset().delete()
        return Response(status=204)
