from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from user.models import User, Contact
from product.models import Product
from .models import Order, OrderedProducts


class TestOrderModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(
            email='testuser@example.com',
            password='password',
            user_role=1,
            first_name='John',
            last_name='Doe',
        )

        # Create a product
        cls.product = Product.objects.create(
            name='Test Product',
            price=10.99,
            description='This is a test product.',
            
        )

    def setUp(self):
        # Create a new order with a pending status
        self.order = Order.objects.create(
            user_id=self.user,
            status='P',
        )

        # Create an ordered product for the order
        self.ordered_product = OrderedProducts.objects.create(
            product_id=self.product,
            order_id=self.order,
            quantity=2,
        )

    def test_order_str_method(self):
        expected_str = f'User ID: {self.user.id}, Order ID: {self.order.id}'
        self.assertEqual(str(self.order), expected_str)

    

    def test_order_created_at_auto_now_add(self):
        # Ensure the created_at field is auto-populated with the current datetime when a new order is created
        now = timezone.now()
        self.assertLess(self.order.created_at, now + timedelta(seconds=1))
        self.assertGreater(self.order.created_at, now - timedelta(seconds=1))

    def test_ordered_product_created_at_auto_now_add(self):
        # Ensure the created_at field is auto-populated with the current datetime when a new ordered product is created
        now = timezone.now()
        self.assertLess(self.ordered_product.created_at, now + timedelta(seconds=1))
        self.assertGreater(self.ordered_product.created_at, now - timedelta(seconds=1))


class TestUserModels(TestCase):

    def setUp(self):
        # Create a contact for the user
        self.contact = Contact.objects.create(
            street_address='123 Test St',
            zip_code='12345',
            state='CA',
            phone_number='209-555-1234',
        )
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='password',
            user_role=1,
            first_name='John',
            last_name='Doe',
        )

    def test_user_str_method(self):
        self.assertEqual(str(self.user), str(self.user.id))

    def test_user_created_at_auto_now_add(self):
        # Ensure the created_at field is auto-populated with the current datetime when a new user is created
        now = timezone.now()
        self.assertLess(self.user.created_at, now + timedelta(seconds=1))
        self.assertGreater(self.user.created_at, now - timedelta(seconds=1))

    def test_user_updated_at_auto_now(self):
        # Ensure the updated_at field is auto-populated with the current datetime when a user is updated
        now = timezone.now()
        self.user.save()
        self.assertLess(self.user.updated_at, now + timedelta(seconds=1))
        self.assertGreater(self.user.updated_at, now - timedelta(seconds=1))

   