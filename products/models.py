from django.db import models


# Create your models here.

class Products_Category(models.Model):
    name = models.CharField('category name', max_length=50)
    def __str__(self):
        return self.name

class Product_Tag(models.Model):
    name = name = models.CharField('category name', max_length=50)
    def __str__(self):
        return self.name

class Nutrients(models.Model):
    MEASUREMENT = [
        ('g', 'gram'),
        ('mg', 'milligram'),
        ('%dv', 'daily value'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField('nutrient name', max_length=50)
    measure = models.CharField('nutrient measurement', max_length=30, choices = MEASUREMENT)
    def __str__(self):
        return self.name

class Products(models.Model):
    SI_UNIT = [
        ('g', 'gram'),
        ('kg', 'kilogram'),
        ('ml', 'ml'),
        ('L', 'liter'),
    ]
    P_UNIT = [
        ('L', 'liter'),
        ('bag', 'bag'),
        ('bottle', 'bottle'),
        ('box', 'box'),
        ('carton', 'carton'),
        ('item', 'item'),
        ('pack', 'pack'),
    ]
    products_id = models.AutoField(primary_key=True)
    name = models.CharField('product name', max_length=120)
    category = models.ForeignKey(Products_Category, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    si_unit = models.CharField('product si unit', max_length=10, choices=SI_UNIT, blank=True)
    quantity_in_si_unit = models.DecimalField('si quantity', max_digits=10, decimal_places=2, null=True, blank=True)
    p_unit = models.CharField('product unit', max_length=10, choices=P_UNIT, blank=True)
    is_active = models.BooleanField(default=False)
    unit_quantity = models.DecimalField('unit quantity', max_digits=10, decimal_places=2)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    on_promotion = models.BooleanField(default=False)
    in_recipe = models.BooleanField(default=False)
    nutrients = models.ManyToManyField(Nutrients, through='Product_Nutrients')
    labels = models.ManyToManyField(Product_Tag)
    last_order_timestamp = models.DateTimeField(auto_now=True)
    image = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Product_Nutrients(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    nutrient_id = models.ForeignKey(Nutrients, null=True, blank=True, on_delete=models.SET_NULL)
    contains = models.DecimalField('nutrients quantity', max_digits=10, decimal_places=2)



