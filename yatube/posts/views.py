from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title
    }
    return render(request, template, context)

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)

def group_posts(reguest, slug):
    template = 'posts/group_posts.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    text = HttpResponse(f'Это группа {slug}')
    context = {
        'title': title,
        'text': text,
    }
    return render(reguest, template, context)

