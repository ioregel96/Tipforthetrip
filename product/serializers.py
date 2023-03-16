from rest_framework import serializers
from .models import Product,ProductImage, FlavorProfile, Review


# Class to serialize Product object data and fixing the format
# of the response message to match id, name, description
class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')
    flavor_profiles = serializers.SerializerMethodField('get_flavor_profiles')
    class Meta:
        model = Product # model used for the Serializer
        fields = '__all__' # serializer format
        #include any images from Product_images
    def get_images(self, obj):
        images = ProductImage.objects.filter(product_id=obj.id)
        serializer = ProductImageSerializer(images, many=True)
        return serializer.data
    def get_flavor_profiles(self, obj):
        flavor_profiles = FlavorProfile.objects.filter(product=obj.id)
        serializer = FlavorProfileSerializer(flavor_profiles, many=True)
        return serializer.data

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage # model used for the Serializer
        fields = '__all__' # serializer format
        #include any images from Product_images

class FlavorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlavorProfile # model used for the Serializer
        fields = '__all__' # serializer format
        #include any images from Product_images

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
