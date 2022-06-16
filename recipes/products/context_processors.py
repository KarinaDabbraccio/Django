# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:26:36 2022

@author: Karina
"""

from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}