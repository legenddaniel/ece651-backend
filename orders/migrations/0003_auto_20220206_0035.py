# Generated by Django 3.2.11 on 2022-02-06 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderproductlist',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order'),
        ),
    ]
