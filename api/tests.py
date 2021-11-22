from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.conf import settings
import requests
class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_invalid_symbol(self):
        """
        Ensure no news for invalid symbol.
        """
        url = 'http://127.0.0.1:8000/news/?format=json&symbol=TVTR'
        response = requests.get(url)
        self.assertEqual(response.status_code,200)
        self.assertIn('"results":[]',response.text)

    def test_get_news(self):
        """
        Ensure we can get news
        """
        url = 'http://127.0.0.1:8000/news/?format=json&symbol=TWTR'
        response = requests.get(url)
        self.assertEqual(response.status_code,200)
        self.assertIn(str("results"),response.text)

    def test_post_method(self):
        """
        Ensure we Cannot POST.
        """
        pload = {'title':'Olivia','description':'123'}
        url = 'http://127.0.0.1:8000/news/?format=json&symbol=TWTR'
        response = requests.post(url, data = pload)
        self.assertEqual(response.status_code,405)

    def test_put_method(self):
        """
        Ensure we Cannot PUT.
        """
        pload = {'title':'Olivia','description':'123'}
        url = 'http://127.0.0.1:8000/news/?format=json&symbol=TWTR'
        response = requests.put(url, data = pload)
        self.assertEqual(response.status_code,405)
