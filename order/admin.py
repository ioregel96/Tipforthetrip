from django.contrib import admin
from .models import Order, OrderedProducts

admin.site.register(Order)
admin.site.register(OrderedProducts)

