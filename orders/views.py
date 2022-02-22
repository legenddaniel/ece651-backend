from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
from django.core.exceptions import FieldDoesNotExist

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
        orders = Order.objects.filter(user=request.user, id=order_id)
        if not orders.count():
            return Response('Order not found', status=status.HTTP_404_NOT_FOUND)

        res = orders.values()[0]
        res['order_items'] = orders[0].order_items.values()

        return Response(res)

    def partial_update(self, request, order_id=None):
        # We don't restore the stocks if order cancelled
        if 'status' in request.data:
            if request.data['status'] not in ('unpaid', 'paid', 'completed', 'cancelled'):
                return Response('Invalid status.', status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.filter(user=request.user, id=order_id)
        if not order.count():
            return Response('Order not found', status=status.HTTP_404_NOT_FOUND)

        try:
            order.update(**request.data)
        except FieldDoesNotExist:
            return Response('Invalid field', status=status.HTTP_400_BAD_REQUEST)

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
        products = []
        qtys = []
        for item in order_items:
            # Verify stock is enough
            product = Product.objects.filter(id=item['product'])
            if not product.count():
                transaction.set_rollback(True)
                return Response('Product id %s does not exist' % item['product'], status=status.HTTP_400_BAD_REQUEST)

            product = product[0]
            if product.stock < item['quantity']:
                transaction.set_rollback(True)
                return Response('Not enough stock for product id %s' % item['product'], status=status.HTTP_400_BAD_REQUEST)

            products.append(product)
            qtys.append(item['quantity'])

            item['unit_price'] = product.price
            item['order'] = order.id
            subtotal += item['quantity'] * item['unit_price']

        serializer = OrderItemSerializer(data=order_items, many=True)
        serializer.is_valid(raise_exception=True)
        order_items = serializer.save()

        # Reduce stocks
        for i in range(len(products)):
            products[i].stock -= qtys[i]
            Product.objects.bulk_update(products, ['stock'])

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
