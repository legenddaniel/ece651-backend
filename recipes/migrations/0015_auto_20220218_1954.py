# Generated by Django 3.2.11 on 2022-02-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_alter_recipe_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrient',
            name='calories',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='carbohydrates',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='cholesterol',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='potassium',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='protein',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='saturated_fat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='saturated fat'),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='sodium',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='total_fat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='total fat'),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='total_fiber',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='total fiber'),
        ),
    ]
