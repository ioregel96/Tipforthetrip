from django.db import models
import django.utils.timezone as timezone
from datetime import datetime
import uuid

# Create your models here.
#gotta be bird and migrate 
#   python ./manage.py makemigrations - Sync Database and Models  
# python ./manage.py migrate - apply migrations  
class NewsPost(models.Model):
    id = models.UUIDField(verbose_name="news_post_id", primary_key=True, default=uuid.uuid4)
    title = models.CharField(verbose_name="title", max_length=100)
    body = models.TextField(verbose_name="body", max_length=5000)
    created_at =models.DateTimeField(verbose_name="created_at",auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="updated_at",auto_now=True, editable=False)

    def __str__(self):
        return self.title
