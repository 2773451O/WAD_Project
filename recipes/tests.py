from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestViews(TestCase):

    def setup(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/home.html')
 