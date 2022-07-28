# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:03:49 2022

@author: Karina
"""

from django.urls import path, reverse_lazy
from . import views
from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    
    #signup
    path('signup/', accounts_views.signup, name='signup'),
    path('ajax/validate_username', views.validate_username, name='validate_username'),
    
    #password change
    path('settings/password/', 
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    
    path('settings/password/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    
    #logout:
    path('logout/', 
         auth_views.LogoutView.as_view(), name='logout'),
    
    #my account update info:
    path('settings/update_account/', 
         accounts_views.UserUpdateView.as_view(), name='update_my_account'),
    
    #my account:
    path('settings/account/', 
         views.my_account_view, name='my_account'),

]
