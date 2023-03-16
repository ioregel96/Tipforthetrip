from django.test import TestCase
from .models import Product
from decimal import Decimal
# Create your tests here.
class ProductTestCase(TestCase):

    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=10.99,
            discount=5            
        )
        self.product = Product.objects.create(
            name="Test Product v2",
            description="This is a test Product v2",
            price=21.33,
            discount=2           
        )

    def test_product_model(self):
        # Test that the product was created with the correct values
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.price,Decimal('10.99'))
        self.assertEqual(product.discount, 5)

        product = Product.objects.get(name="Test Product v2")
        self.assertEqual(product.description, "This is a test Product v2")
        self.assertEqual(product.price,Decimal('21.33'))
        self.assertEqual(product.discount,2)