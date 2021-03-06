# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:28:04 2022

@author: Karina
"""

from django import forms
from .models import Recipe, Comment

class NewRecipeForm(forms.ModelForm):
    #this would refer to the field in the other model that should be saved
    #from this form
    #comment = forms.CharField(widget=forms.Textarea(), max_length=1000)
    
    rec_description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 10, 'placeholder': 'Describe the process and ingredients. Maximum 1000 symbols. ',
                   'class': 'form-input'}
            ),
        max_length=1000,
        #help_text='The max length of the text is 1000.'
    )

    class Meta:
        model = Recipe
        # fields correspond to the fields in Model
        fields = ['subject', 'cooking_time', 'rec_description']
        
        
class CommentForm(forms.ModelForm):
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 6, 'class': 'form-input', 'autofocus': ''}
            ),
        max_length=1000,
        #help_text='The max length of the text is 1000.'
    )
    
    class Meta:
        model = Comment
        fields = ['message' ]