from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from accounts.models import Profile

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        orders = Order.objects.all().order_by('-date_ordered')
        
        # create the list of all ordered items: key-Product, value - unitsOrdered: quantity
        ordered_items_list = dict()
        labelsk = []
        datak = []
        for order in orders:
            oredred_products = order.get_ordered_products()
            for op in oredred_products:
                name = op.product
                #price = op.price
                quantity = op.quantity
                ordered_items_list[name] = ordered_items_list.get(name, 0) + quantity
        
        for k,v in ordered_items_list.items():
            labelsk.append(k.name)
            datak.append(v)
            
        #pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(orders, 10)
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
        
        #print(ordered_items_list.values())
        #for key in ordered_items_list.keys():
        #    print(key.price)
        
    return render(request, 'sales/all_orders.html', {'orders': orders, 
                                                     'ordered_items_list': ordered_items_list, 
                                                     'labels': labelsk,
                                                        'data': datak, })

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderUpdForm(request.POST)
        if form.is_valid():
            order_f = form.save(commit=False)
            order.paid_amount = order_f.paid_amount
            order.picked_up = order_f.picked_up
            order.save()
            return redirect('sales:all_orders')
    else:
        form = OrderUpdForm(instance=order)
    
    return render(request, 'sales/order_details.html', {'order': order,
                                                       'form': form})