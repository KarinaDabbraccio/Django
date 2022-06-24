# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:47:17 2022

@author: Karina
"""

from django import forms
from .models import InventoryItem, Manufacturer, Location

class InventoryModelForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['product', 'amount', 'cost', 'sell_by', 'location', 'manufacturer']