# Generated by Django 4.1.2 on 2023-02-09 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]