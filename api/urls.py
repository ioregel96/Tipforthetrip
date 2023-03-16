from django.urls import path, include

urlpatterns = [
    path('users/', include('user.urls')),
    path('products/', include('product.urls')),
    path('news/', include('newspost.urls')),
    path('page_content/', include('pagecontent.urls')),
    path('orders/', include('order.urls'))
]

