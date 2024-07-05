from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#HTTP REQUEST

def home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Carlos Eduardo'
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return render(request, 'recipes/sobre.html')