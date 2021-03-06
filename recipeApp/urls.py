"""recipeApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from recipe.views import recipeAddForm, recipeList, workInProgress, viewRecipe
from grocery.views import groceryLists, groceryListAdd, viewGroList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('addRecipe', recipeAddForm, name='addRecipe'),
    path('recipeList', recipeList, name='recipeList'),
    path('workInProgress', workInProgress, name='workInProgress'),
    path('groceryLists', groceryLists, name='groceryLists'),
    path('groceryListAdd', groceryListAdd, name='groceryListAdd'),
    path('viewGroList/<int:list_id>', viewGroList, name='viewGroList'),
    path('viewRecipe/<int:recipe_id>', viewRecipe, name='viewRecipe'),
]
