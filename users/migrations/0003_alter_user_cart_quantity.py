# Generated by Django 4.0.1 on 2022-01-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_cart',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
