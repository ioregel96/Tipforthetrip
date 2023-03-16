from django.db import models
from datetime import datetime
from product.models import Product
from user.models import User
import uuid


STATUS_CHOICES = [
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('C', 'Completed'),
        ('T', 'Terminated'),
        
    ]
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return f'User ID: {self.user_id}, Order ID: {self.id}'

class OrderedProducts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return f'Product ID: {self.product_id}, Order ID: {self.order_id}'

