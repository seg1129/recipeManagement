from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.forms import formset_factory

from .models import Recipe
from .forms import RecipeForm


def recipeAddForm(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipeList')
    else:
        form = RecipeForm()
    return render(request, 'addRecipe.html', {'form': form})


def recipeList(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes': recipes})

def viewRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'viewRecipe.html', {'recipe': recipe})

def workInProgress(request):
    return render(request, 'workInProgress.html')
