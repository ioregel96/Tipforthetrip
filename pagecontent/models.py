from django.db import models
import django.utils.timezone as timezone
from datetime import datetime
import uuid

class NewsPage(models.Model):
    # Max length of a URL in the address bar is 2048, [, editable=False] to make required
    id = models.UUIDField(verbose_name="News Page ID", primary_key=True, default=uuid.uuid4, editable=False)
    background_img = models.URLField(verbose_name="Background Image", max_length=2049)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "News Page"

class HistoryPage(models.Model):
    id = models.UUIDField(verbose_name="History Page ID", primary_key=True, default=uuid.uuid4, editable=False)
    background_img = models.URLField(verbose_name="Background Image", max_length=2049)
    history_title = models.TextField(verbose_name="History Title", max_length=1000)
    history_summary = models.TextField(verbose_name="History Summary", max_length=1000)
    top_left_video_title = models.TextField(verbose_name="Top Left Video Title", max_length=1000)
    top_left_video_link = models.URLField(verbose_name="Top Left Video Link", max_length=2049)
    top_right_video_title = models.TextField(verbose_name="Top Right Video Title", max_length=1000)
    top_right_video_link = models.URLField(verbose_name="Top Right Video Link", max_length=2049)
    bottom_left_video_title = models.TextField(verbose_name="Bottom Left Video Title", max_length=1000)
    bottom_left_video_link = models.URLField(verbose_name="Bottom Left Video Link", max_length=2049)
    bottom_right_video_title = models.TextField(verbose_name="Bottom Right Video Title", max_length=1000)
    bottom_right_video_link = models.URLField(verbose_name="Bottom Right Video Link", max_length=2049)
    def __str__(self):
        return str(self.history_page_id)
        
    class Meta:
        verbose_name_plural = "History Page"
    
class HomePage(models.Model):
    id = models.UUIDField(verbose_name="Home Page ID", primary_key=True, default=uuid.uuid4, editable=False)
    left_img = models.URLField(verbose_name="Left Image Link", max_length=2049)
    right_img = models.URLField(verbose_name="Right Image Link", max_length=2049)
    right_img_title = models.TextField(verbose_name="Right Image Title", max_length=100)
    right_img_description = models.TextField(verbose_name="Right Image Description", max_length=1000)
    bottom_img = models.URLField(verbose_name="Bottom Image Link", max_length=2049)
    mission_statement = models.TextField(verbose_name="Mission Statement Text", max_length=1000)
    def str(self):
        return str(self.home_page_id)
    class Meta:
        verbose_name_plural = "Home Page"
    