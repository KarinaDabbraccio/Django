from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm, ProfileForm
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from orders.models import Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

MAX_DISCOUNT = 5
AMOUNT_FOR_MAX_DISCOUNT = 500
AVER_DISCOUNT = 2
AMOUNT_FOR_AVER_DISCOUNT = 250

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with THIS username already exists.'
    return JsonResponse(data)
    

def my_account_view(request):
    #show user's orders - filter by this user
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    total = 0
    discount = request.user.profile.user_discount
    n_discount = 0;

    #if still less than max discount
    if discount < MAX_DISCOUNT:
        for order in orders:
            total += order.get_total()
            if total > AMOUNT_FOR_MAX_DISCOUNT:
                break
        if total >= AMOUNT_FOR_MAX_DISCOUNT:
            n_discount = MAX_DISCOUNT
        elif total >= AMOUNT_FOR_AVER_DISCOUNT:
            n_discount = AVER_DISCOUNT
        if discount!= n_discount and discount < n_discount:
            discount = n_discount
            request.user.profile.user_discount = discount
            request.user.profile.save()
           
    if discount > 0:
        message = "Discount is " + str(discount) +"%"
    else:
        message = "Spend $" + str(AMOUNT_FOR_AVER_DISCOUNT - total) +" more to get a customer discount."
        
    #pagination for orders - now 3 because don't have much
    page = request.GET.get('page', 1)
    paginator = Paginator(orders, 4)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    
    #picture upload here
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.pic = form.cleaned_data.get('pic')
            request.user.profile.save()
            return redirect('accounts:my_account')
    else:
        form = ProfileForm()
    return render(request, 'accounts/my_account.html', {'orders':orders, 'form': form, 'message': message, 'total': total})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/update_my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user

