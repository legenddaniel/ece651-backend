from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField('category name', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "product category"
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = name = models.CharField('tag name', max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name


class Nutrient(models.Model):
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


class Product(models.Model):
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
    product_id = models.AutoField(primary_key=True)
    name = models.CharField('product name', max_length=120)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
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
    nutrients = models.ManyToManyField(Nutrient, through='products.ProductNutrient')
    labels = models.ManyToManyField(ProductTag)
    last_order_timestamp = models.DateTimeField(auto_now=True)
    image = models.URLField(max_length=500)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ('-product_id',)

    def __str__(self):
        return self.name



class ProductNutrient(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    nutrient_id = models.ForeignKey(Nutrient, null=True, blank=True, on_delete=models.SET_NULL)
    contains = models.DecimalField('nutrients quantity', max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.product_id) + " - " + str(self.nutrient_id)



