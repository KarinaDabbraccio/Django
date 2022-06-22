from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from inventory.models import InventoryItem, LossInventory
import datetime
from django.views.generic import DeleteView, CreateView, UpdateView


@login_required
def manage_inv(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        #orders = Order.objects.filter(inProduction=False)
        items = InventoryItem.objects.all()
        today = datetime.date.today()
        expired = InventoryItem.objects.filter(sell_by__lte=today)
                
    return render(request, 'inventory/manage_inv.html', {'items' : items, 'expired': expired})

@login_required
def delete_expired(request):
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

    return render(request, 'inventory/delete_expired_done.html', {'count' : count, 'total': total, 'lost_list': lost_list})