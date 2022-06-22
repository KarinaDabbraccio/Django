from django.shortcuts import render, redirect, get_object_or_404
from products.models import PricedProduct
from django.db.models import Count

from django.views.decorators.http import require_POST

from .models import OrderedProduct
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart


# CART 
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(PricedProduct, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('orders:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(PricedProduct, product_id=product_id)
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
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderedProduct.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order_new_done.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_new.html',
                  {'cart': cart, 'form': form})