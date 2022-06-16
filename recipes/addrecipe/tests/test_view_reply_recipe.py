# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:18:21 2022

@author: Karina
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..forms import CommentForm
from ..models import Category, Recipe, Comment
from ..views import reply_recipe


class ReplyRecipeTestCase(TestCase):
    '''
    Base test case to be used in all `reply_recipe` view tests
    '''
    def setUp(self):
        self.category = Category.objects.create(name='Test', description='Test category.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.recipe = Recipe.objects.create(subject='Some food', cooking_time='20', category=self.category, starter=user)
        Comment.objects.create(message='Lorem ipsum dolor sit amet', recipe=self.recipe, created_by=user)
        self.url = reverse('addrecipe:reply_recipe', kwargs={'pk': self.category.pk, 'recipe_pk': self.recipe.pk})


class LoginRequiredReplyRecipeTests(ReplyRecipeTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class ReplyRecipeTests(ReplyRecipeTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CommentForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 1)
        self.assertContains(self.response, '<textarea', 1)


class SuccessfulReplyRecipeTests(ReplyRecipeTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'message': 'Some food'})

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        recipe_comments_url = reverse('addrecipe:recipe_comments', kwargs={'pk': self.category.pk, 'recipe_pk': self.recipe.pk})
        self.assertRedirects(self.response, recipe_comments_url)

    def test_reply_created(self):
        '''
        The total comment count should be 2
        The one created in the `ReplyRecipeTestCase` setUp
        and another created by the comment data in this class
        '''
        self.assertEquals(Comment.objects.count(), 2)


class InvalidReplyRecipeTests(ReplyRecipeTestCase):
    def setUp(self):
        '''
        Submit an empty dictionary to the `reply_recipe` view
        '''
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)