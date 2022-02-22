# Generated by Django 3.2.11 on 2022-02-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_recipe_ingredients_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('chinese', 'Chinese'), ('english', 'English'), ('maxican', 'Maxican'), ('indian', 'Indian'), ('thai', 'Thai'), ('indonesian', 'Indonesian'), ('middleeast', 'Middle East'), ('italian', 'Italian'), ('japanese', 'Japanese'), ('korean', 'Korean'), ('vietnamese', 'Vietnamese'), ('northamerican', 'North American'), ('greek', 'Greek')], max_length=30),
        ),
    ]