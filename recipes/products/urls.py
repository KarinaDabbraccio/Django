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

] 