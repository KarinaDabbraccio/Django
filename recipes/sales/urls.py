# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:30:47 2022

@author: Karina
"""

from django.urls import path
from . import views


app_name = 'sales'
urlpatterns = [
    
    path('all_orders/', views.all_orders, name='all_orders'),
    
    ]