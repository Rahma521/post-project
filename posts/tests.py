from django.test import TestCase
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self) :
        Post.objects.create(text="just a text")

    def testTextContext(self):
        post = Post.get(id=1)
        expected_text = post.text
        self.assertEqual(expected_text, "just a text")

class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text="this s a home page test")

    def testViewUrlRedirectProperLocation(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def testViewUrlByName(self):
        resp = self.client.get(reversed("home"))
        self.assertEqual(resp.status_code, 200)

    def testViewUsesCorrectTemplate(self):
        resp = self.client.get(reversed("home"))
        self.assertTemplateUsed(resp, "home,html")

