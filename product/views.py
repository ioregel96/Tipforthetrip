from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductImage, Review
from .serializers import ProductSerializer, ProductImageSerializer, ReviewSerializer

import uuid

# Create your views here.
# ? Gets items by the product_id
@api_view(['GET'])
def get_item_by_id(request, uuid_str):
    try:
        uid_hex = uuid.UUID(uuid_str).hex #parse passed in UUID to verify that the pid is in correct UUID format
        product = Product.objects.get(pk=uid_hex)
        serialized_product = ProductSerializer(product)
        return Response({'data': {'ok': True, "product": serialized_product.data}})
    except:
        return Response({'data': {'ok': False, uuid_str: "No product found with this id."}}, status=400)

# ? Get all items
@api_view(['GET'])
def get_items(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(products)
    return Response({'data': {'ok': True,"products": serializer.data}})

# Add review
def add_review(request, uuid_str):
    try:
        uid_hex = uuid.UUID(uuid_str).hex
        product = Product.objects.get(pk=uid_hex)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product_id=product)
            return Response({'data': {'ok': True, 'message': 'Review added successfully.'}})
        return Response({'data': {'ok': False, 'message': 'Invalid data.'}}, status=400)
    except:
        return Response({'data': {'ok': False, uuid_str: "No product found with this id."}}, status=400)