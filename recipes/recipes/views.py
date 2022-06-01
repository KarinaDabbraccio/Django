# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:13:31 2022

@author: Karina
"""

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world. You're at the RECIPES index.")
    return render(request, 'index.html')
