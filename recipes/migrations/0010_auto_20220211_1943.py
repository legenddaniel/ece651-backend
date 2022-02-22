# Generated by Django 3.2.11 on 2022-02-11 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20220211_1801'),
        ('recipes', '0009_auto_20220206_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.CharField(max_length=50)),
                ('total_fat', models.CharField(max_length=50, verbose_name='total fat')),
                ('saturated_fat', models.CharField(max_length=50, verbose_name='saturated fat')),
                ('cholesterol', models.CharField(max_length=50)),
                ('sodium', models.CharField(max_length=50)),
                ('total_fiber', models.CharField(max_length=50, verbose_name='total fiber')),
                ('protein', models.CharField(max_length=50)),
                ('carbohydrates', models.CharField(max_length=50)),
                ('potassium', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutrient',
            field=models.ManyToManyField(to='recipes.Nutrient'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='products',
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='recipe_products', through='recipes.ProductQuantity', to='products.Product')
        )
    ]