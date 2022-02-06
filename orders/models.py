from django.db import models
from django.utils import timezone
from products.models import Product
from users.models import User
# Create your models here.


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    timestamp = models.DateTimeField('order time', default=timezone.now)
    total_price = models.DecimalField(
        'total price', max_digits=20, decimal_places=2)

    def __str__(self):
        return "{}, {}".format(self.user_id, self.order_id)


class OrderProductList(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product_id = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order_id) + " - " + str(self.product_id)
