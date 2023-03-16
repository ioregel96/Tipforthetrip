from rest_framework import serializers
from .models import NewsPage, HistoryPage, HomePage

# Class to serialize Page_Content object data and fixing the format
# of the response message to match id, name, description
class NewsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPage # model used for the Serializer
        fields = '__all__' # serializer format

class HistoryPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryPage # model used for the Serializer
        fields = '__all__' # serializer format

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage # model used for the Serializer
        fields = '__all__' # serializer format
