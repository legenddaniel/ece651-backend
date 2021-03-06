# Generated by Django 3.2.11 on 2022-02-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_custom_migrations'),
        ('recipes', '0006_alter_recipe_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='recipe_products', to='products.Product'),
        ),
    ]
