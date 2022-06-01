from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category

def addrecipe(request):
    #return HttpResponse("Hello, world. You're at the ADDRECIPE index.")
    
    categories = Category.objects.all()
    """ categories_names = list()

    for category in categories:
        categories_names.append(category.name)

    response_html = '<br>'.join(categories_names)

    return HttpResponse(response_html)"""

    return render(request, 'addrecipe.html', {'categories': categories})
