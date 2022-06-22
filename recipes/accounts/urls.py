# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:03:49 2022

@author: Karina
"""

from django.urls import path
from . import views
from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [

    #login-signup
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    #password reset views
    path('reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
   
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    
    #password change
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    
    #logout:
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    #my account update info:
    path('settings/update_account/', accounts_views.UserUpdateView.as_view(), name='update_my_account'),
    
    #my account:
    path('settings/account/', views.my_account_view, name='my_account'),

]
