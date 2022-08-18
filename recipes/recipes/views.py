# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:13:31 2022

@author: Karina
"""

from django.shortcuts import render
#from django.contrib.auth.models import User
from accounts.models import Profile

#from orders.models import OrderedProduct
from products.models import Group, Product
from orders.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
#from inventory.models import InventoryItem


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
    return render(request, 'home.html', {'donePro' : donePro })

    View includes optional content for managers only , 
    all product groups for all users
    """
    groups = Group.objects.all()
    currentUser = "Anonymous"    
    if request.user.is_authenticated:
        currentUser = Profile.objects.get(username_id=request.user)

    return render(request, 'home.html', {'currentUser' : currentUser, 'groups': groups })

def group_products(request, pk):
    group = get_object_or_404(Group, pk=pk)
    products = group.products.order_by('-name')
    return render(request, 'group_products.html', {'group': group, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_details.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
