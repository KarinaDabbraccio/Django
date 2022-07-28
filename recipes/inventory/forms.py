# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:47:17 2022

@author: Karina
"""

from django import forms
from .models import InventoryItem, Manufacturer, Location
from datetime import timedelta, date


class InventoryModelForm(forms.ModelForm):
    # set default in a week from today, min date is tomorrow
    minday = date.today() + timedelta(days=1)
    valday = date.today() + timedelta(days=7)
    sell_by = forms.DateField(widget=forms.TextInput(attrs={'min': minday, 'value': valday, 'type': 'date'}), required=True)
    
    class Meta:
        model = InventoryItem
        fields = ['product', 'amount', 'cost', 'sell_by', 'location', 'manufacturer']