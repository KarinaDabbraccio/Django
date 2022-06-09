# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:06:55 2022

@author: Karina
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Category, Recipe, Comment
from ..views import recipe_comments


class RecipeCommentsTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Test', description='Test category.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        recipe = Recipe.objects.create(subject='Some food', category=category, cooking_time='20', starter=user)
        Comment.objects.create(message='It was tasty but long', recipe=recipe, created_by=user)
        url = reverse('addrecipe:recipe_comments', kwargs={'pk': category.pk, 'recipe_pk': recipe.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/addrecipe/1/recipes/1/')
        self.assertEquals(view.func, recipe_comments)