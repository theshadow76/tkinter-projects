from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home():
    template = loader.get_template('vetoffice/home.html')
    return HttpResponse(template.render())