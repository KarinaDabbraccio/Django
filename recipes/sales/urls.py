# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:30:47 2022

@author: Karina
"""

from django.urls import path
from . import views


app_name = 'sales'
urlpatterns = [
    
    path('all-orders-m/', views.all_orders, name='all_orders'),
    path('details-upd/<int:order_id>/', views.order_details, name='order_details'),

    ]