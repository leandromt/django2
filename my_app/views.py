from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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


def post_list(request):
    data_page = {
        'title': 'Listagem de posts',
        'description': 'Esta página lista todos os posts',
        'posts': Post.objects.all()
    }
    return render(request, 'posts/post_list.html', data_page)


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'posts/post_show.html', {'post': post})
