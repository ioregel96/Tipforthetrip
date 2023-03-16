from django.contrib import admin
from .models import Product, ProductImage, FlavorProfile, Review

class ProductImageInline(admin.TabularInline):
    readonly_fields = ('created_at',)
    list_display = ('product_id', 'img_url', 'created_at')
    model = ProductImage

class FlavorProfileInline(admin.TabularInline):
    model = FlavorProfile.product.through
    list_display = ('name',)
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('id', 'name', 'price', 'created_at')
    inlines = [
        ProductImageInline,
        FlavorProfileInline,
    ]

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('id', 'rating', 'comment', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(FlavorProfile)
admin.site.register(Review, ReviewAdmin)




