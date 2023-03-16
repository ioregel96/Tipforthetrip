from django.test import TestCase
from newspost.models import  NewsPost
# Create your tests here.

class newspostModelTestCase(TestCase):
    def setUp(self):
        NewsPost.objects.create(
            title="Test Title",
            body="This is a test newspost.",
        )
        NewsPost.objects.create(
            title="Test Title new2",
            body="This is a test newspost new2.",
        )

    def test_newspost(self):
        post = NewsPost.objects.get(title="Test Title")
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.body, "This is a test newspost.")

        post = NewsPost.objects.get(title="Test Title new2")
        self.assertEqual(post.title, "Test Title new2")
        self.assertEqual(post.body, "This is a test newspost new2.")
