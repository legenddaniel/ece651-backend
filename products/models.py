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
    name = models.CharField('tag name', max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    SI_UNIT = [
        ('g', 'gram'),
        ('kg', 'kilogram'),
        ('ml', 'ml'),
        ('L', 'liter'),
        ('lb', 'pound'),
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
    name = models.CharField('product name', max_length=120)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    si_unit = models.CharField('product si unit', max_length=10, choices=SI_UNIT, blank=True)
    unit_quantity = models.DecimalField('si quantity', max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    on_promotion = models.BooleanField(default=False)
    in_recipe = models.BooleanField(default=False)
    labels = models.ManyToManyField(ProductTag, blank=True)
    last_order_timestamp = models.DateTimeField(auto_now=True)
    image_url = models.URLField(max_length=500)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name



