# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:26:45 2022

@author: Karina
"""

from django import forms
from .models import Order


class OrderUpdForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'paid' , 'delivered'
            ]
        
