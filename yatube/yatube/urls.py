from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Добавляем к путям из приложения posts пространство имён posts
    # namespace для избавления проблем с одинаковыми именами name
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
