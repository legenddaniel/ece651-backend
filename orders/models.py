from django.db import models
from django.utils import timezone
from products.models import Products
from users.models import User
# Create your models here.
class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('order time', default=timezone.now)
    total_price = models.DecimalField('total price', max_digits=20, decimal_places=2)

class Order_Product_List(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()

