from .models import Group, Product
from orders.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
from inventory.models import InventoryItem

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
