from django.db import models
from products.models import Product
from users.models import User
# Create your models here.
class UserCart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    quantity = models.IntegerField()
    def __str__(self):
        product_name = ", ".join(str(seg) for seg in self.product_id.all())
        return "{}, {}".format(self.user_id, product_name)