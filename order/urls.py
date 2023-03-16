from django.urls import path
from .views import OrderView, OrderItemsView

urlpatterns = [
    path('', OrderView.as_view()),
    path('<slug:pk>/', OrderView.as_view()),
    
    path('items/', OrderItemsView.as_view()),
    path('items/slug:pk>/', OrderItemsView.as_view())
    
]
