from django.forms import ModelForm
from django import forms
from .models import Recipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'source', 'instructions']
        ingredients = forms.ModelMultipleChoiceField(queryset=None)

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'type', 'amount']
# forms.ModelMultipleChoiceField
