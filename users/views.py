from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import ShippingAddress

from .serializers import ShippingAddressSerializer, UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.request.user

    def partial_update(self, request, pk=None):
        if 'shipping_address' not in request.data:
            return super().partial_update(request, pk)

        address = request.user.shipping_address
        address_serializer = ShippingAddressSerializer(
            address, data={'user': request.user.id, **request.data['shipping_address']})
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()
        return self.retrieve(request, pk)


class ShippingAddressView(ModelViewSet):
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)

    def get_object(self):
        return ShippingAddress.objects.get(user=self.request.user)

    def put(self, request):

        ship_update = ShippingAddress.objects.filter(user=request.user).first()
        request.data['user'] = request.user.id
        serializer = ShippingAddressSerializer(
            ship_update, data=request.data)  # instance = new_add
        message = {}

        if serializer.is_valid():
            serializer.save()
            message["success"] = "updated"
            return Response(data=message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
