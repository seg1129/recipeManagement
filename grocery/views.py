from django.shortcuts import render, redirect

from .models import GroceryList
from recipe.models import Recipe
from .forms import GroceryListForm

def groceryLists(request):
    lists = GroceryList.objects.all()
    return render(request, 'groceryList.html', {'lists': lists})

def groceryListAdd(request):
    if request.method == 'POST':
        form = GroceryListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('groceryLists')
    else:
        print("we are getting to grocery views in else")
        form = GroceryListForm()
    return render(request, 'addGroList.html', {'form': form})

def getGroceryList(recipe):
    ingreds = []
    ingredients_object = Recipe.objects.filter(pk=recipe).values('ingredient1',
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

    ingred_list = list(ingredients_object)

    if (ingred_list[0]['ingredient1']):
        ingreds.append(ingred_list[0]['ingredient1'])
    if (ingred_list[0]['ingredient2']):
        ingreds.append(ingred_list[0]['ingredient2'])
    if (ingred_list[0]['ingredient3']):
        ingreds.append(ingred_list[0]['ingredient3'])
    if (ingred_list[0]['ingredient4']):
        ingreds.append(ingred_list[0]['ingredient4'])
    if (ingred_list[0]['ingredient5']):
        ingreds.append(ingred_list[0]['ingredient5'])
    if (ingred_list[0]['ingredient6']):
        ingreds.append(ingred_list[0]['ingredient6'])
    if (ingred_list[0]['ingredient7']):
        ingreds.append(ingred_list[0]['ingredient7'])
    if (ingred_list[0]['ingredient8']):
        ingreds.append(ingred_list[0]['ingredient8'])
    if (ingred_list[0]['ingredient9']):
        ingreds.append(ingred_list[0]['ingredient9'])
    if (ingred_list[0]['ingredient10']):
        ingreds.append(ingred_list[0]['ingredient10'])
    if (ingred_list[0]['ingredient11']):
        ingreds.append(ingred_list[0]['ingredient11'])
    if (ingred_list[0]['ingredient12']):
        ingreds.append(ingred_list[0]['ingredient12'])
    if (ingred_list[0]['ingredient13']):
        ingreds.append(ingred_list[0]['ingredient13'])
    if (ingred_list[0]['ingredient14']):
        ingreds.append(ingred_list[0]['ingredient14'])
    if (ingred_list[0]['ingredient15']):
        ingreds.append(ingred_list[0]['ingredient15'])

    return list(ingreds)

def viewGroList(request, list_id):
    ingredients = []
    groceryList = {}

    # get recipes and grocery list name from the database
    recipes = GroceryList.objects.filter(pk=list_id).values('recipes')
    grocery_list_name = list(GroceryList.objects.filter(pk=list_id).values('name'))

    # get ingredients from the recipes
    for recipe in list(recipes):
        ingredients = ingredients + getGroceryList(recipe['recipes'])

    groceryList['ingredients'] = ingredients
    groceryList['name'] = grocery_list_name[0]['name']
    return render(request, 'newGroList.html', {'groceryList': groceryList})
