# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:28:24 2022

@author: Karina
"""

from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initialize
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}         
        self.cart = cart
        
    def add(self, product, quantity=1, update_quantity=False):
        """
        Add product to cart or increase its quantity if already there
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                 'price': str(product.price)}
        if update_quantity:
           self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # refresh session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # cancel session as 'changed to be sure it's saved
        self.session.modified = True
        
    def remove(self, product):
        """
        Remove Product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
           del self.cart[product_id]
           self.save()
           
    def __iter__(self):
        """
       Iterate in cart and get products from the data base
        """
        product_ids = self.cart.keys()
        # get products and add them to cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
           item['price'] = Decimal(item['price'])
           item['total_price'] = item['price'] * item['quantity']
           yield item
           
    def __len__(self):
        """
        Count products in cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        count total for the rpoducts in cart
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
               self.cart.values())
    
    def clear(self):
        # delete cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True