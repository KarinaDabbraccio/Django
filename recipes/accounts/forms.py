# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:52:02 2022

@author: Karina
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['pic'].label = 'Update profile picture:'
    
    class Meta:
        model = Profile
        fields = ('pic', )      