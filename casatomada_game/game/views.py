#Llamadas a modulos de django
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

