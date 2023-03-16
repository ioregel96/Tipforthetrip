from django.test import TestCase
from user.models import User

class UserModels(TestCase):
    def test_createUser(self):
        user = User.objects.create(email="ee@ee.com", password="password123", user_role="0", first_name="EE", last_name="GG")
        self.assertEqual(str(user), str(user))

class ContactModels(TestCase):
    def createContact(self):
        contact = Contact.objects.create(street_address="123 street avenue", zip_code="12345", state="California", phone_number="1234567890")
        self.assertEqual(str(contact), contact)