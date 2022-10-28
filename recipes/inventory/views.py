from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from inventory.models import InventoryItem, LossInventory
from orders.models import Order
import datetime

from .forms import InventoryModelForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        total_cost_expired=0
        
        for item in expired:
            total_cost_expired+=item.cost * item.amount
        
        for item in items:
            product=item.product
            amount=item.amount
            total_cost+=item.cost * amount
            groups_inventory_list[product] = groups_inventory_list.get(product , 0) + amount
        
        # create the chart data
        labelsk = []
        datak = []       
        for k,v in groups_inventory_list.items():
            labelsk.append(k.name)
            datak.append(v)    
        
        #pagination for the list of inventory items
        page = request.GET.get('page', 1)
        paginator = Paginator(items, 6)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
                
    return render(request, 'inventory/manage_inv.html', {'expired': expired,'items': items,
                                                         'groups_inventory_list': groups_inventory_list,
                                                         'total_cost': total_cost,
                                                         'total_cost_expired': total_cost_expired,
                                                         'labels': labelsk,
                                                         'data': datak, })                


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
                return redirect('inventory:manage_inv')
        else:
            form = InventoryModelForm()
    
    return render(request, 'inventory/create_inv.html', {'form': form})



                
                
                
                
                