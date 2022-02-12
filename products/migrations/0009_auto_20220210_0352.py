# Generated by Django 3.2.11 on 2022-02-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220206_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity_in_si_unit',
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrients',
            field=models.ManyToManyField(blank=True, null=True, through='products.ProductNutrient', to='products.Nutrient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='si quantity'),
        ),
    ]
