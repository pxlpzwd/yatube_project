from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('не главная')

"""
# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}') 
"""
