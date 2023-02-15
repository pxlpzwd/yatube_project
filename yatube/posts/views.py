from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = {
        'title': title,
        'text': 'Последние обновления на сайте'
    }
    return render(request, template, context) 


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции.!!11!'
    }
    return render(request, template, context)


