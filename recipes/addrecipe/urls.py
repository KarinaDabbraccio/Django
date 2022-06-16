# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:03:49 2022

@author: Karina
"""

from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'addrecipe'
urlpatterns = [
    path('', views.add_recipe, name='add_recipe'),
    path('<int:pk>/', views.category_recipes, name='category_recipes'),
    path('<int:pk>/new/', views.new_recipe, name='new_recipe'),
    path('<pk>/recipes/<int:recipe_pk>/', views.recipe_comments, name='recipe_comments'),
    path('<pk>/recipes/<int:recipe_pk>/reply/', views.reply_recipe, name='reply_recipe'),

]
