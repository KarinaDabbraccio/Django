
from . import views
from django.urls import include, path


app_name = 'inventory'
urlpatterns = [

    path('manage_inv/', views.manage_inv, name='manage_inv'),
    path('delete_expired/', views.delete_expired, name='delete_expired'),
    path('create/', views.create_inv, name='create_inv'),
    
]

