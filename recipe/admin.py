from django.contrib import admin

from .models import IngredientType, Ingredient, Recipe

admin.site.register(IngredientType)

admin.site.register(Ingredient)

admin.site.register(Recipe)
