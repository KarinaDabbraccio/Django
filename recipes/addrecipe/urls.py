# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:03:49 2022

@author: Karina
"""

from django.urls import path
from . import views


app_name = 'addrecipe'
urlpatterns = [
    path('', views.addrecipe, name='addrecipe'),
]


    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),