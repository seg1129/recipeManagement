from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

# from .models import Question
# ...
def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
