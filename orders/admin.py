from django.contrib import admin
from .models import  Order, OrderProductList

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderProductList)

