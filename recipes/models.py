from django.contrib.postgres.fields import ArrayField
from django.db import models
from products.models import Products#, Nutrients

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
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField('recipe name',max_length=50)
    description = models.TextField(blank=True)
    rating = models.DecimalField('rating', max_digits=3, decimal_places=1)
    cuisine = models.CharField(max_length=30, choices=CUISINE)    #incoming choices from ML team
    label = models.ManyToManyField(Label)
    products = models.ManyToManyField(Products)
    instructions = ArrayField(models.CharField(max_length=200))
    last_purchase_made = models.DateTimeField(auto_now=True)
    # nutrients = models.ManyToManyField(Nutrients, through='Recipe_Nutrients')
    total_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# class User_Fav_Recipe(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     no_purchased = models.IntegerField(default=0)
# class Recipe_Nutrients(models.Model):
#     recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     nutrient_id = models.ForeignKey(Nutrients, null=True, blank=True, on_delete=models.SET_NULL)
#     contains = models.DecimalField('nutrients quantity', max_digits=10, decimal_places=2)

