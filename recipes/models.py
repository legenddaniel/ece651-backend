from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
from products.models import Product#, Nutrients

# Create your models here.
class Label(models.Model):
    recipe_label = models.CharField(max_length=30)
    def __str__(self):
        return self.recipe_label

class Recipe(models.Model):
    CUISINE = [
        ('chinese', 'Chinese'),
        ('english', 'English'),
        ('maxican', 'Maxican'),
        ('indian', 'Indian'),
        ('thai', 'Thai'),
        ('indonesian', 'Indonesian'),
        ('middleeast', 'Middle East'),
    ]
    name = models.CharField('recipe name',max_length=50)
    description = models.TextField(blank=True)
    rating = models.DecimalField('rating', max_digits=3, decimal_places=1)
    cuisine = models.CharField(max_length=30, choices=CUISINE)    #incoming choices from ML team
    label = models.ManyToManyField(Label, null=True, blank=True)
    image_url = models.URLField(max_length=500)
    products = models.ManyToManyField(Product, through='ProductQuantity', through_fields=('recipe','product'), related_name='recipe_products')
    instructions = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    last_purchase_made = models.DateTimeField(auto_now=True)
    total_reviews = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class ProductQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    def __str__(self):
        return self.recipe.name + ' - ' + self.product.name

class Nutrient(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    calories = models.CharField(max_length=50)
    total_fat = models.CharField('total fat', max_length=50)
    saturated_fat = models.CharField('saturated fat', max_length=50)
    cholesterol = models.CharField(max_length=50)
    sodium = models.CharField(max_length=50)
    total_fiber = models.CharField('total fiber', max_length=50)
    protein = models.CharField(max_length=50)
    carbohydrates = models.CharField(max_length=50)
    potassium = models.CharField(max_length=50)
    def __str__(self):
        return self.recipe.name

