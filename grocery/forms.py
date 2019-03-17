from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import GroceryList
from recipe.models import Recipe

class GroceryListForm(ModelForm):
    class Meta:
        model = GroceryList
        fields = ['name', 'recipes']
    def __init__(self, *args, **kwargs):
        super(GroceryListForm, self).__init__(*args, **kwargs)
        self.fields['recipes'] =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)
