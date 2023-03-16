from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import NewsPage, HomePage, HistoryPage
from .serializers import NewsPageSerializer, HistoryPageSerializer, HomePageSerializer
from .views import GrabPageContentAll, GrabPageContent
import uuid

# Create your tests here.
# class NewsTestCase(TestCase):
#     def test_news_save(self):
#         news = NewsPage(backgroundImg="https://assets.stickpng.com/images/580b57fcd9996e24bc43c51f.png")

#         news.save()
#         saved_news = NewsPage.objects.get(backgroundImg="https://assets.stickpng.com/images/580b57fcd9996e24bc43c51f.png")
#         self.assertEqual(saved_news.backgroundImg, "https://assets.stickpng.com/images/580b57fcd9996e24bc43c51f.png")

class NewsPageModelTestCase(TestCase):
    def setUp(self):
        self.news_page = NewsPage.objects.create(background_img="https://example.com/news_bg.jpg")
    
    def test_news_page_str_method(self):
        self.assertEqual(str(self.news_page), str(self.news_page.id))

class GrabPageContentAllTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_all_page_content(self):
        url = reverse('grab_page_content_all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertTrue('news_content' in response.data)
        self.assertTrue('history_content' in response.data)
        self.assertTrue('home_content' in response.data)
        self.assertTrue('status' in response.data)


