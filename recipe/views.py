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
        print("we are getting to views in else")
        form = RecipeForm()
        # form2 = IngredientForm()
        # form2 = (formset_factory(IngredientForm, can_delete=False, extra=1))
    return render(request, 'addRecipe.html', {'form': form})
# def recipeAddForm(request):
#     template = loader.get_template('addRecipe.html')
#     context = {}
#     print(template)
#     return HttpResponse(template.render(context, request))

def recipeList(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes': recipes})

def viewRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'viewRecipe.html', {'recipe': recipe})

def workInProgress(request):
    return render(request, 'workInProgress.html')
