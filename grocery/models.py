from django.db import models

from recipe.models import Recipe

class GroceryList(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name
