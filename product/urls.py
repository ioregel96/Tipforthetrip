from django.urls import path
from .views import get_item_by_id, get_items

urlpatterns = [
    path('', get_items, name='items'),
    path('<slug:uuid_str>/', get_item_by_id, name='item_by_id'),
]

