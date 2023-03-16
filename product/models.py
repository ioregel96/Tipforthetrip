from django.db import models
import django.utils.timezone as timezone
from datetime import datetime
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(verbose_name="product id", primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name="name", max_length=50)
    description = models.TextField(verbose_name="description", max_length=1000)
    price = models.DecimalField(verbose_name="price", max_digits=8, decimal_places=2)
    discount = models.IntegerField(verbose_name="discount", default=100)
    created_at = models.DateTimeField(verbose_name="created_at",auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="updated_at",auto_now=True, editable=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    # product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    img_url = models.CharField(verbose_name="img url", max_length=255)
    created_at = models.DateTimeField(verbose_name="created_at",auto_now_add=True, editable=False)

    def __str__(self):
        return self.img_url

class FlavorProfile(models.Model):
    name = models.CharField(verbose_name="name", max_length=50)
    product = models.ManyToManyField(Product,verbose_name="product(s)", blank=True)
    created_at = models.DateTimeField(verbose_name="created_at",auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="updated_at",auto_now=True, editable=False)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE_STAR = 1, ('1 star')
        TWO_STARS = 2, ('2 stars')
        THREE_STARS = 3, ('3 stars')
        FOUR_STARS = 4, ('4 stars')
        FIVE_STARS = 5, ('5 stars')

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RatingChoices.choices)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
