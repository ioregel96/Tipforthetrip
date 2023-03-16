from rest_framework import serializers
from .models import NewsPost

# Class to serialize Product object data and fixing the format
# of the response message to match id, name, description
class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost # model used for the Serializer
        fields = '__all__' # serializer format