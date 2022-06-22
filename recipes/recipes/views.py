# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:13:31 2022

@author: Karina
"""

from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import Profile

def home(request):
    """
    This code was used after extension of User Model to create Profile 
    for existing users. Not needed after.
    
    donePro = False
    users = User.objects.all()
    for username in users:
        obj, created = Profile.objects.get_or_create(username=username)
        print(username.username,' : ',created)
    print("all done")
    return render(request, 'home.html', {'donePro' : donePro })"""
    currentUser = "Anonymous"    
    if request.user.is_authenticated:
        currentUser = Profile.objects.get(username_id=request.user)

    return render(request, 'home.html', {'currentUser' : currentUser })
