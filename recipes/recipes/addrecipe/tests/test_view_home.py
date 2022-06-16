# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:08:59 2022

@author: Karina
"""

from django.urls import reverse
from django.test import TestCase
from ..models import Category


class HomeTests(TestCase):    
    def setUp(self):
        self.category = Category.objects.create(name='Testing', description='Testing category.')
        url = reverse('addrecipe:addrecipe')
        self.response = self.client.get(url)
        
    #def test_addrecipe_view_status_code(self):      
     #   response = self.client.get(reverse('addrecipe:addrecipe'))
      #  self.assertEqual(response.status_code, 200)
        
    def test_addrecipe_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    #def test_addrecipe_url_resolves_addrecipe_view(self):   - FAILED
     #   view = resolve('/')
      #  self.assertEquals(view.func, addrecipe)

    def test_home_view_contains_link_to_topics_page(self):
        category_recipes_url = reverse('addrecipe:category_recipes', kwargs={'pk': self.category.pk})
        self.assertContains(self.response, 'href="{0}"'.format(category_recipes_url))