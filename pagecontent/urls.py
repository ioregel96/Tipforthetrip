from django.urls import path, include
from .views import GrabPageContentAll, GrabPageContent
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('', GrabPageContentAll.as_view(), name='grab_page_content_all'),
    path('<str:page>/', GrabPageContent.as_view(), name='grab_page_content'),
    # path('news/<uuid:pk>/', GrabNewsPageItemByID.as_view(), name='grab_news_item'),   
    # path('history/<uuid:pk>/', GrabHistoryPageItemByID.as_view(), name='grab_news_item'),
    # path('home/<uuid:pk>/', GrabHomePageItemByID.as_view(), name='grab_news_item'),
]

