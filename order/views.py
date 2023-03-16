from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderedProducts
from .serializers import OrderSerializer, OrderedProductSerializer
from rest_framework.decorators import api_view


class OrderView(APIView):
    def get(self, request, pk=None):
        if pk:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemsView(APIView):
    def get(self, request, pk=None):
        if pk:
            OrderedProducts = OrderedProducts.objects.get(pk=pk)
            serializer = OrderedProductSerializer(OrderedProducts)
            return Response(serializer.data)
        else:
            OrderedProducts = OrderedProducts.objects.all()
            serializer = OrderedProductSerializer(OrderedProducts, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = OrderedProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        OrderedProducts = OrderedProducts.objects.get(pk=pk)
        serializer = OrderedProductSerializer(OrderedProducts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        OrderedProducts = OrderedProducts.objects.get(pk=pk)
        OrderedProducts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def get_item_by_id(request, id):
#     orderitem = OrderedProducts.objects.filter(id=id).first()
#     serializer = Prod(OrderedProducts)
#     if serializer.data["user_name"] == "":
#         return Response({'data': {'ok': False, id: None}})
#     return Response({'data': {'ok': True, id: serializer.data}})
