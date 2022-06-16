# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:13:31 2022

@author: Karina
"""

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

