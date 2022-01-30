# Generated by Django 4.0.1 on 2022-01-30 16:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='recipe name')),
                ('description', models.TextField(blank=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='rating')),
                ('cuisine', models.CharField(choices=[('chinese', 'Chinese'), ('english', 'English'), ('maxican', 'Maxican'), ('indian', 'Indian'), ('thai', 'Thai'), ('indonesian', 'Indonesian'), ('middleeast', 'Middle East')], max_length=30)),
                ('instructions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('last_purchase_made', models.DateTimeField(auto_now=True)),
                ('total_views', models.IntegerField(default=0)),
                ('label', models.ManyToManyField(to='recipes.Label')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]
