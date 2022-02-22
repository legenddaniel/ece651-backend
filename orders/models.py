from django.db import models

from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from users.models import User
from products.models import Product


class Order(TimeStampedModel, StatusModel):
    STATUS = Choices('unpaid', 'paid', 'completed', 'cancelled')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{}, {}".format(self.user, self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.order) + " - " + str(self.product)
