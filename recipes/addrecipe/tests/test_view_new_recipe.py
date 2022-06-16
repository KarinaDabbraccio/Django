# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:11:19 2022

@author: Karina
"""

from django.urls import reverse
from django.test import TestCase
from ..models import Category, Recipe
from  django.contrib.auth.models import User
from ..forms import NewRecipeForm

    
class NewRecipeTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Testing', description='Testing category.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')

    def test_new_recipe_view_success_status_code(self):
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_recipe_view_not_found_status_code(self):
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_recipe_view_contains_link_back_to_category_recipes_view(self):
        new_recipe_url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        category_recipes_url = reverse('addrecipe:category_recipes', kwargs={'pk': 1})
        response = self.client.get(new_recipe_url)
        self.assertContains(response, 'href="{0}"'.format(category_recipes_url))
        
    def test_csrf(self):
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_recipe_valid_post_data(self):
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        data = {
            'subject': 'Test title',
            'cooking_time': '20',
            'rec_description': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Recipe.objects.exists())
       
    def test_contains_form(self):  # <- new test
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewRecipeForm)

    def test_new_recipe_invalid_post_data(self): 
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)


class LoginRequiredNewRecipeTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Test', description='Test category.')
        self.url = reverse('addrecipe:new_recipe', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))