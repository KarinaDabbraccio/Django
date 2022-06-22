# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:32:02 2022

@author: Karina
"""


from django import forms
from .models import InventoryItem

class DeleteInventoryForm(forms.ModelForm):
    
    class Meta:
        model = InventoryItem
        fields = ['amount']