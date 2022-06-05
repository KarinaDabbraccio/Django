from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Category, Recipe, Comment
from .forms import NewRecipeForm
from django.contrib.auth.decorators import login_required


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

@login_required
def new_recipe(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit = False)
            recipe.category = category
            recipe.starter = request.user 
            recipe.save()
            #here would be saving the second Model - post
            """post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )"""
            return redirect('addrecipe:category_recipes', pk=category.pk)  # TODO: redirect to the created topic page
    else:
        form = NewRecipeForm()


    return render(request, 'new_recipe.html', {'category': category, 'form': form})
