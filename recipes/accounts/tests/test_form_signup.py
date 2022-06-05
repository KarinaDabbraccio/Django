# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:23:49 2022

@author: Karina
"""

from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)