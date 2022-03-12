from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import FieldDoesNotExist

from .serializers import CartItemSerializer
from .models import CartItem


class CartItemView(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(user=self.request.user)

    # Add one item to cart
    def create(self, request):
        items = request.data if isinstance(
            request.data, list) else [request.data]
        serializer = CartItemSerializer(
            data=[{'user': request.user.id, **item} for item in items], many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return self.list(request)

    # Update one cart item (e.g. quantity). Do deletion if quantity goes 0.
    def partial_update(self, request, pk=None):
        items = CartItem.objects.filter(user=request.user, id=pk)
        if not items.count():
            return Response('Cannot find this cart item.', status=status.HTTP_404_NOT_FOUND)

        if 'quantity' in request.data and request.data['quantity'] == 0:
            items.delete()
        else:
            try:
                items.update(**request.data)
            except FieldDoesNotExist:
                return Response('Invalid field', status=status.HTTP_400_BAD_REQUEST)

        return self.list(request)

    # Clear cart for current user
    def destroy(self, request):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
