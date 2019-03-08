from django.db import models


class IngredientType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    source = models.CharField(max_length=200, blank=False)
    instructions = models.TextField()

    def __str__(self):
        return self.name
