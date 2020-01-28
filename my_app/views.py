from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# MVC
# M - models.py
# V - html
# C - views.py

# MTV
# Models - models.py
# Template - templates
# Veiw - views.py (controllers)


def home(request):
    return HttpResponse('Olá Mundo!')


def home_para(request):
    return HttpResponse('Olá Mundo!')
