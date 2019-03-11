from django.contrib import admin

from .models import IngredientType, Recipe

admin.site.register(IngredientType)

# admin.site.register(Ingredient)

admin.site.register(Recipe)
