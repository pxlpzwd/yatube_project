from django.shortcuts import render, get_object_or_404
from .models import Group, Post

# Главная страница
def index(request):
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'text': 'Последние обновления на сайте'
    }
    return render(request, template, context) 


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Здесь будет информация о группах проекта Yatube"
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции.!!11!' 
    }
    return render(request, template, context)