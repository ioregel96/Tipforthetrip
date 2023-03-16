from rest_framework import serializers
from .models import Order, OrderedProducts
from product.serializers import ProductSerializer
from product.models import Product

class OrderSerializer(serializers.ModelSerializer):
    products_in_order = serializers.SerializerMethodField('get_products')
    class Meta:
        model = Order
        fields = '__all__'
    def get_products(self, obj):
        products_orders = OrderedProducts.objects.filter(order_id=obj.id)
        serializer = OrderedProductSerializer(products_orders, many=True)
        return serializer.data



class OrderedProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField('get_product')
    class Meta:
        model = OrderedProducts
        fields = ['id', 'product_id', 'order_id', "quantity", "created_at", "product"]
    def get_product(self, obj):
        # product_id is a reference to the Product Model object
        # the ".id" will pull the actual id from the model since
        # TODO: look into changing the object so the model can be referenced as "product" and not "product_id"
        pid = obj.product_id.id

        product = Product.objects.get(id=pid) # ? This simply works. . .  
        serializer = ProductSerializer(product)
        return serializer.data