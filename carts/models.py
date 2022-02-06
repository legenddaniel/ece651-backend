from django.db import models
from products.models import Product
from users.models import User

from model_utils.models import TimeStampedModel


class CartItem(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cart_items')

    # May discuss the behavior when cart item is off shelf. Now follow order item.
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "{}, {}".format(self.user__id, self.product)
