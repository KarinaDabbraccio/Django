from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from accounts.models import Profile
from inventory.models import InventoryItem

from django.views.generic import UpdateView
from .forms import OrderUpdForm


@login_required
def all_orders(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        # get not processsed orders
        #orders = Order.objects.filter(shipped=False, paid=False).order_by('created')
        orders = Order.objects.all().order_by('created')
        # create the list of all ordered items: key-Product, value - unitsOrdered: quantity
        ordered_items_list = dict()
        for order in orders:
            oredred_products = order.get_ordered_products()
            for op in oredred_products:
                name = op.product
                price = op.price
                quantity = op.quantity
                ordered_items_list[name] = ordered_items_list.get(name, 0) + quantity
                

                
        print("________________ALL!!!")
        # {<PricedProduct: Chocolate - Gr: IceCream - 7.50>: 18, ... <PricedProduct: Chocolate Crumbs - Gr: Cookies - 8.00>: 1}
        print(ordered_items_list.values())
        print('price')
        for key in ordered_items_list.keys():
            print(key.price)
        
    return render(request, 'sales/all_orders.html', {'orders': orders, 
                                                     'ordered_items_list': ordered_items_list})

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderUpdForm(request.POST)
        if form.is_valid():
            order_f = form.save(commit=False)
            order.paid = order_f.paid
            order.shipped = order_f.shipped
            order.save()
            return redirect('sales:order_details', order_id=order.id)
    else:
        form = OrderUpdForm(instance=order)
    
    return render(request, 'sales/order_details.html', {'order': order,
                                                       'form': form})