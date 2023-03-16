from django.contrib import admin
from .models import NewsPost
# Register your models here.

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    # readonly_fields will allow non-editable fields to show up in the Admin portal
    readonly_fields = ("id", "created_at", "updated_at")

# admin.site.register(Product, ProductAdmin)