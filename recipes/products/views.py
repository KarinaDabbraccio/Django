from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Product
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.views.decorators.http import require_POST

from .models import OrderedProduct
from .forms import CartAddProductForm, OrderCreateForm
from .cart import Cart


def products_all(request):
    groups = Group.objects.all()
    return render(request, 'products/products_all.html', {'groups': groups})

def group_products(request, pk):
    group = get_object_or_404(Group, pk=pk)
    products = group.products.order_by('-name')
    return render(request, 'products/group_products.html', {'group': group, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product_details.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


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
    return redirect('products:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('products:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'products/cart_detail.html', {'cart': cart})

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
            return render(request, 'products/order_new_done.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'products/order_new.html',
                  {'cart': cart, 'form': form})