from django.forms import ModelForm
from django import forms
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        ingredients = forms.ModelMultipleChoiceField(queryset=None)
