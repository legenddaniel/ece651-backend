from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_producttag_slug'),
    ]

    operations = [
        TrigramExtension(),
    ]