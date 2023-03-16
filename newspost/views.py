from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NewsPost
from .serializers import NewsPostSerializer

import uuid

# Create your views here


# ? Get all news
@api_view(['GET'])
def get_news(request):
    news = NewsPost.objects.all()
    news_serialized = NewsPostSerializer(news, many=True).data
    print(news_serialized)
    return Response({'data': {'ok': True,"news": news_serialized}})