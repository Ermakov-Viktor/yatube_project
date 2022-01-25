from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница Виктора')

def group_posts(reguest, slug):
    return HttpResponse(f'Это группа {slug}')
