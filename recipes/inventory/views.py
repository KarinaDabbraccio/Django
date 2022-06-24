from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from inventory.models import InventoryItem, LossInventory
from orders.models import Order
import datetime
from django.views.generic import DeleteView, CreateView, UpdateView

from .forms import InventoryModelForm


@login_required
def manage_inv(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        items = InventoryItem.objects.all()
        today = datetime.date.today()
        expired = InventoryItem.objects.filter(sell_by__lte=today)
        
        groups_inventory_list=dict()        
        total_cost=0
        
        for item in items:
            product=item.product
            amount=item.amount
            total_cost+=item.cost * amount
            groups_inventory_list[product] = groups_inventory_list.get(product , 0) + amount
                
    return render(request, 'inventory/manage_inv.html', {'expired': expired,'items': items,
                                                         'groups_inventory_list': groups_inventory_list,
                                                         'total_cost': total_cost})

@login_required
def delete_expired(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        today = datetime.date.today()
        lost_list = InventoryItem.objects.filter(sell_by__lte=today)
      
        count=0
        total = 0
        for item in lost_list:
            count+=1

            LossInventory.objects.create(product = item.product,
                                         amount = item.amount,
                                         cost = item.cost,
                                         location = item.location,
                                         manufacturer = item.manufacturer)
            total+= (item.amount * item.cost)
    
            expired = InventoryItem.objects.filter(sell_by__lte=today).delete()

        return render(request, 'inventory/delete_expired_done.html', 
                      {'count' : count, 'total': total, 'lost_list': lost_list})
 
    
@login_required
def create_inv(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        if request.method == 'POST':
            form = InventoryModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = InventoryModelForm()
    
    return render(request, 'inventory/create_inv.html', {'form': form})


def deliver_ordered(request):
    """From all available Inventory subtract ordered
    Method for inventory - FIFO - first sell the items that were registered earlier
    """
    # extract expired
    today = datetime.date.today()
    items = InventoryItem.objects.exclude(sell_by__lte=today).order_by('registered_at')
    
    orders = Order.objects.filter(inProduction=False).order_by('created')
    items = InventoryItem.objects.all().order_by('cost')
    
    ordered_items_list = dict()
    
    for order in orders:
        oredred_products = order.get_ordered_products()
        for op in oredred_products:
            product = op.product
            price = op.product.price
            quantity = op.quantity
            ordered_items_list[product] = ordered_items_list.get(product, 0) + quantity
            
    print("________________ALL!!!")
    # {<PricedProduct: Chocolate - Gr: IceCream - 7.50>: 18, ... <PricedProduct: Chocolate Crumbs - Gr: Cookies - 8.00>: 1}
    print(ordered_items_list.values())
    print(ordered_items_list.keys())
    print('price')
    for key in ordered_items_list.keys():
        print(key.price)

                
                
                
                
                