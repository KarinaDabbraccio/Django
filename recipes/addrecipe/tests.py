from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import addrecipe

class HomeTests(TestCase):
    def test_addrecipe_view_status_code(self):      
        response = self.client.get(reverse('addrecipe:addrecipe'))
        self.assertEqual(response.status_code, 200)
        
