from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Вместо конкретного адреса в шаблонах можно использовать name = '', в тегах адресов {% url %}: 
    path('', views.index, name = 'index'),
    path('group/<slug>/', views.group_posts, name = 'group_posts'),
] 