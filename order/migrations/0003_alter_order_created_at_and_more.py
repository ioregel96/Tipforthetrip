# Generated by Django 4.1.2 on 2023-03-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderedproducts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
