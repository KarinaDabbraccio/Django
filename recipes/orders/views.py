from django.shortcuts import render, redirect, get_object_or_404
#from products.models import PricedProduct
from products.models import Product
from django.db.models import Count

from django.views.decorators.http import require_POST

from .models import OrderedProduct
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart
import math
from inventory.models import InventoryItem


# CART 
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('orders:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/cart_detail.html', {'cart': cart})

#ORDER
def order_new(request):
    cart = Cart(request)
     
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        inv_cost=0
        if form.is_valid():
            
            inv_del_list = list()
            inv_upd_list = list()
            # check that it is enough inventory
            
            for item in cart:
                product_cart = item['product']
                quantity_cart = item['quantity']
                print(product_cart)
                print(quantity_cart)
                
                if quantity_cart > product_cart.is_instock():
                    #one of the products is not enough in stock - deny order, keep the cart with all stuff
                    print()
                    msg = "Product is not enought in stock: " + product_cart.name
                    print(msg)
                    return render(request, 'orders/order_new.html', {'cart': cart, 'form': form, 'msg':msg})
                    
                else:    
                    # add to list to remove from the inventory 
                    inv_list = InventoryItem.objects.filter(product=product_cart)
                    for inv in inv_list:
                        inv_quantity=inv.amount
                        
                        if quantity_cart > 0:
                            inv.amount-=quantity_cart
                            #update cost
                            if inv_quantity >= quantity_cart:
                                inv_cost+= inv.cost * quantity_cart
                            else:
                                inv_cost+= inv.cost * inv_quantity
                               
                            quantity_cart-=inv_quantity                     
                            
                            if inv.amount <= 0:
                                #delete inventoryItem with 0 amount
                                #inv.delete()
                                inv_del_list.append(inv)                                
                            else:
                                #save updated inventoryItem
                                #inv.save()
                                inv_upd_list.append(inv)
                        else:
                        #exit loop when deleted/updated as much as ordered
                            break
            
            #update the database
            for inv in inv_del_list:
                inv.delete()
            for inv in inv_upd_list:
                inv.save()
            
            #after check that all items are enough, save new order and process cart    
            order = form.save()
            order.inventory_total_cost = inv_cost
            order.save()
            for item in cart:
                #create ordered product
                OrderedProduct.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear cart
            cart.clear()
            return render(request, 'orders/order_new_done.html',
                          {'order': order, 'inv_cost' : inv_cost})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_new.html',
                  {'cart': cart, 'form': form})