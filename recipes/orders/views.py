from django.shortcuts import render, redirect, get_object_or_404
#from products.models import PricedProduct
from products.models import Product

from django.views.decorators.http import require_POST

from .models import OrderedProduct
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart
from decimal import Decimal
from inventory.models import InventoryItem


# CART 
@require_POST
def cart_add(request, product_id):
    """ Add this product to cart, appears on the product_detail page
    """
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
    """ Remove this product from cart, appears as link in the cart_detail
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')

def cart_detail(request):
    """ If user not logged in: show cart details only
    If logged in: show cart detail and Order Form
    """
    cart = Cart(request)
    discount = 0
    to_pay = 0 
    if request.user.is_authenticated:
        discount = request.user.profile.user_discount
        to_pay = Decimal(cart.get_total_price() * Decimal(1 - discount/100)).quantize(Decimal('1.00'))
        
    #discount = request.user.profile.user_discount
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
                    msg = "The product is not enought in stock: " + product_cart.name
                    print(msg)
                    return render(request, 'orders/cart_order.html', {'cart': cart, 'form': form, 'msg':msg})
                    
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
            order = form.save(commit=False)
            order.inventory_total_cost = inv_cost
            #apply discount
            to_pay = cart.get_total_price() * Decimal(1 - discount/100)
            order.paid_amount = to_pay
            order.user = request.user
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
                          {'order': order, 'inv_cost' : inv_cost, 'discount':discount})
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(instance = request.user)
        else:
            form = 0
    return render(request, 'orders/cart_order.html',
                  {'cart': cart, 'form': form, 'discount':discount, 'to_pay':to_pay})
