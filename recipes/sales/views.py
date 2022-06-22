from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order
from accounts.models import Profile
from inventory.models import InventoryItem


@login_required
def all_orders(request):
    #check to see who is logged in
    current_user = Profile.objects.get(username_id=request.user)
    current_user_group = getattr(current_user, 'user_group')
    # if current user is not manager, redirect to home
    if (current_user_group != 'M'):
        return redirect('home')
    else:
        orders = Order.objects.filter(inProduction=False)
        items = InventoryItem.objects.all()
        
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
        print(ordered_items_list)
    
        
    return render(request, 'sales/all_orders.html', {'orders': orders, 'items' : items, })