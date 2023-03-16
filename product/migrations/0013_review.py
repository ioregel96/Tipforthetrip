# Generated by Django 4.1.2 on 2023-02-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_product_flavor_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
