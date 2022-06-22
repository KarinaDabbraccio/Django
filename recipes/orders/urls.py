# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:24:02 2022

@author: Karina
"""

from django.urls import path
from . import views


app_name = 'orders'
urlpatterns = [
    
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('new/', views.order_new, name='order_new'),
] 