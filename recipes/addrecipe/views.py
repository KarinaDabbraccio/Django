from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Recipe, Comment
from .forms import NewRecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count



def add_recipe(request):   
    categories = Category.objects.all()
    return render(request, 'addrecipe/addrecipe.html', {'categories': categories})

def category_recipes(request, pk):
    category = get_object_or_404(Category, pk=pk)
    recipes = category.recipes.order_by('-last_updated').annotate(replies=Count('comments'))
    return render(request, 'addrecipe/recipes.html', {'category': category, 'recipes': recipes})

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
            return redirect('addrecipe:recipe_comments', pk=pk, recipe_pk=recipe.pk)
    else:
        form = NewRecipeForm()


    return render(request, 'addrecipe/new_recipe.html', {'category': category, 'form': form})

def recipe_comments(request, pk, recipe_pk):
    recipe = get_object_or_404(Recipe, category__pk=pk, pk=recipe_pk)
    recipe.views += 1
    recipe.save()
    return render(request, 'addrecipe/recipe_comments.html', {'recipe': recipe})

@login_required
def reply_recipe(request, pk, recipe_pk):
    recipe = get_object_or_404(Recipe, category__pk=pk, pk=recipe_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.created_by = request.user
            comment.save()
            return redirect('addrecipe:recipe_comments', pk=pk, recipe_pk=recipe_pk)
    else:
        form = CommentForm()
    return render(request, 'addrecipe/reply_recipe.html', {'recipe': recipe, 'form': form})

