from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#HTTP REQUEST

def home(request):
    return render(request,'recipes/pages/home.html', context={
        'name': 'Carlos Eduardo'
    })

def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', context={
        'name': 'Carlos Eduardo'
    })