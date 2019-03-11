from django.shortcuts import render


from .models import GroceryList
from recipe.models import Recipe
from .forms import GroceryListForm

# def selectRecipe(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'selectRecipe.html', {'recipes': recipes})

def groceryLists(request):
    lists = GroceryList.objects.all()
    return render(request, 'groceryList.html', {'lists': lists})

def groceryListAdd(request):
    if request.method == 'POST':
        form = GroceryListForm(data=request.POST)
        if form.is_valid():
            form.save()
            print(form)
            # getGroceryList(form)
            return render(request, 'groceryList.html')
    else:
        print("we are getting to grocery views in else")
        form = GroceryListForm()
        # form2 = IngredientForm()
        # form2 = (formset_factory(IngredientForm, can_delete=False, extra=1))
    return render(request, 'addGroList.html', {'form': form})

def getGroceryList(recipe):
    print(recipe)
    ingreds = []
    ingreds = Recipe.objects.filter(pk=recipe).values('ingredient1',
                                                        'ingredient2',
                                                        'ingredient3',
                                                        'ingredient4',
                                                        'ingredient5',
                                                        'ingredient6',
                                                        'ingredient7',
                                                        'ingredient8',
                                                        'ingredient9',
                                                        'ingredient10',
                                                        'ingredient11',
                                                        'ingredient12',
                                                        'ingredient13',
                                                        'ingredient14',
                                                        'ingredient15')
    print("ingredients in getGroceryList")
    print(list(ingreds))
    for item in list(ingreds):
        for ingredient in list(item):
            print(ingreds )
            if (ingredient != ''):
                ingreds.append(ingredient)
    # print(ingreds)
    return list(ingreds)

def viewGroList(request, list_id):
    ingredients = []
    print(request)
    print(list_id)
    recipes = GroceryList.objects.filter(pk=list_id).values('recipes')
    for recipe in list(recipes):
        ingredients.append(getGroceryList(recipe['recipes']))
    # recipe = Recipe.objects.get(pk=list_id)
    print("ok final list of ingredients")
    print(ingredients)
    return render(request, 'addGroList.html')
