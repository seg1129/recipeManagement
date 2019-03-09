from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.forms import formset_factory
# from data.models import
from .forms import RecipeForm, IngredientForm


def recipeAddForm(request):
    if request.method == 'POST':
        form = RecipeForm()
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("we are getting to views in else")
        form = RecipeForm()
        # form2 = IngredientForm()
        form2 = (formset_factory(IngredientForm, can_delete=False, extra=1))
    return render(request, 'addRecipe.html', {'form': form, 'form2': form2})
# def recipeAddForm(request):
#     template = loader.get_template('addRecipe.html')
#     context = {}
#     print(template)
#     return HttpResponse(template.render(context, request))
