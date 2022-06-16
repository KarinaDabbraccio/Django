# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:24:02 2022

@author: Karina
"""

from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    
    path('all/', views.products_all, name='products_all'),
    path('<int:pk>/', views.group_products, name='group_products'),
    path('details/<int:product_id>/', views.product_details, name='product_details'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('order/', views.order_new, name='order_new'),
] 