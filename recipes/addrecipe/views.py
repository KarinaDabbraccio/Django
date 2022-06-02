from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from .models import Category, Recipe, Comment
from django.http import Http404

def addrecipe(request):
    #return HttpResponse("Hello, world. You're at the ADDRECIPE index.")
    
    categories = Category.objects.all()
    """ categories_names = list()

    for category in categories:
        categories_names.append(category.name)

    response_html = '<br>'.join(categories_names)

    return HttpResponse(response_html)"""

    return render(request, 'addrecipe.html', {'categories': categories})

def category_recipes(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'recipes.html', {'category': category})

def new_recipe(request, pk):
    category = get_object_or_404(Category, pk=pk)
    #return render(request, 'new_recipe.html', {'category': category})
    
    if request.method == 'POST':
        subject = request.POST['subject']
        cooktime = request.POST['cooktime']
        ls = request.POST['lowsugar']
        if (ls == 'on'):
            low_sugar = True
        else:
               low_sugar = False 
        rec_description = request.POST['description']
        

        user = User.objects.first()  
        # TODO: get the currently logged in user

        recipe = Recipe.objects.create(
            subject=subject,
            rec_description = rec_description,
            category=category,
            starter=user,
            lowsugar = low_sugar,
            cooking_time = cooktime
        )

        """post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )"""

        return redirect('addrecipe:category_recipes', pk=category.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_recipe.html', {'category': category})