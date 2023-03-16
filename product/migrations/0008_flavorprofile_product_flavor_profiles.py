# Generated by Django 4.1.2 on 2023-02-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlavorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='flavor_profiles',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.flavorprofile'),
        ),
    ]
