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
    path('', views.addrecipe, name='addrecipe'),
    #url(r'^addrecipe', views.addrecipe, name='addrecipe'),
    url(r'^(?P<pk>\d+)/$', views.category_recipes, name='category_recipes'),
    url(r'^(?P<pk>\d+)/new/$', views.new_recipe, name='new_recipe'),
    url(r'^(?P<pk>\d+)/recipes/(?P<recipe_pk>\d+)/$', views.recipe_comments, name='recipe_comments'),
    url(r'^(?P<pk>\d+)/recipes/(?P<recipe_pk>\d+)/reply/$', views.reply_recipe, name='reply_recipe'),


]


    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),