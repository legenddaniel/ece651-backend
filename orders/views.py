from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from decimal import Decimal

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order
from products.models import Product
from carts.models import CartItem


class OrderView(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def retrieve(self, request, order_id=None):
        order = Order.objects.filter(
            user=request.user, id=order_id).values()[0]
        return Response(order)

    def partial_update(self, request, order_id=None):
        if 'status' in request.data:
            if request.data['status'] not in ('unpaid', 'paid', 'completed', 'cancelled'):
                return Response(status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.filter(user=request.user, id=order_id)
        order.update(**request.data)

        return self.list(request)

    # Create an order
    @transaction.atomic
    def create(self, request):

        # Create order
        order = {
            "user": request.user.id,
            "STATUS": request.data['status'] or 'unpaid',
            "subtotal": 0,
            "tax": 0,
            "total": 0,
        }

        serializer = OrderSerializer(data=order)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        # Create order items and bind to the order
        order_items = request.data['order_items']
        subtotal = Decimal(0)
        products = set()
        for item in order_items:
            item['unit_price'] = Product.objects.get(id=item['product']).price
            item['order'] = order.id
            subtotal += item['quantity'] * item['unit_price']
            products.add(item['product'])

        serializer = OrderItemSerializer(data=order_items, many=True)
        serializer.is_valid(raise_exception=True)
        order_items = serializer.save()

        # Update the order money info
        TAX = Decimal(0.13)
        order.subtotal = subtotal
        order.tax = subtotal * TAX
        order.total = subtotal * (1 + TAX)
        order.save()

        # Remove cart items
        cart_items = CartItem.objects.filter(
            user=request.user, product__in=products)
        cart_items.delete()

        return self.list(request)
