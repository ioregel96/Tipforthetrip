from django.shortcuts import render
from rest_framework.views import APIView
from .models import NewsPage, HistoryPage, HomePage
from rest_framework.response import Response
from .serializers import NewsPageSerializer, HistoryPageSerializer, HomePageSerializer

# Create your views here.
class GrabPageContentAll(APIView):
    def get(self, request):
        news_content = NewsPage.objects.all()
        history_content = HistoryPage.objects.all()
        home_content = HomePage.objects.all()
        serializer =({
            "news_content": NewsPageSerializer(news_content, many=True).data,
            "history_content": HistoryPageSerializer(history_content, many=True).data,
            "home_content": HomePageSerializer(home_content, many=True).data,
            "status": "success"
        })
        return Response(serializer)

class GrabPageContent(APIView):
    def get(self, request, page):
        if page == "news":
            page_content = NewsPage.objects.get()
            serializer = NewsPageSerializer(page_content)
            return Response({'data': {'ok': True, page: serializer.data}})
        elif page == "history":
            page_content = HistoryPage.objects.get()
            serializer = HistoryPageSerializer(page_content)
            return Response({'data': {'ok': True, page: serializer.data}})
        elif page == "home":
            page_content = HomePage.objects.get()
            serializer = HomePageSerializer(page_content)
            return Response({'data': {'ok': True, page: serializer.data}})
        else:
            return Response({'data': {'ok': False, "error": "no existing page"}})

# class GrabPageContent(APIView):
#     def get(self, request, page):
#         if page == "news":
#             page_content = NewsPage.objects.get(news_page_content_id=page)
#             serializer = NewsPageSerializer(page_content)
#             return Response({'data': {'ok': True, page: serializer.data}})
#         elif page == "history":
#             page_content = HistoryPage.objects.get(history_page_id=page)
#             serializer = HistoryPageSerializer(page_content)
#             return Response({'data': {'ok': True, page: serializer.data}})
#         elif page == "home":
#             page_content = HomePage.objects.get(home_page_id=page)
#             serializer = HomePageSerializer(page_content)
#             return Response({'data': {'ok': True, page: serializer.data}})
#         else:
#             return Response({'data': {'ok': False, "error": "no existing page"}})

# class GrabNewsPageItemByID(APIView):
#     def get(self, request, pk):
#         try:
#             news_item = NewsPage.objects.get(pk=pk)
#             serializer = NewsPageSerializer(news_item)
#             return Response({'data': {'ok': True, 'news_item': serializer.data}})
#         except NewsPage.DoesNotExist:
#             return Response({'data': {'ok': False, 'error': 'news item not found'}})
        
# class GrabHistoryPageItemByID(APIView):
#     def get(self, request, pk):
#         try:
#             history_item = HistoryPage.objects.get(pk=pk)
#             serializer = HistoryPageSerializer(history_item)
#             return Response({'data': {'ok': True, 'history_item': serializer.data}})
#         except NewsPage.DoesNotExist:
#             return Response({'data': {'ok': False, 'error': 'history item not found'}})

# class GrabHomePageItemByID(APIView):
#     def get(self, request, pk):
#         try:
#             home_item = HomePage.objects.get(pk=pk)
#             serializer = HomePageSerializer(home_item)
#             return Response({'data': {'ok': True, 'home_item': serializer.data}})
#         except NewsPage.DoesNotExist:
#             return Response({'data': {'ok': False, 'error': 'home item not found'}})
             