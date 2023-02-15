from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Объявляем класс Group, наследник класса Model из пакета models
# Далее описываем поля модели и их типы
class Group(models.Model):

    title = models.CharField(
        max_length=200,
        )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        )
    description = models.TextField(
        max_length=400,
    )

    def __str__(self):
        return self.title


# Объявляем класс Post, наследник класса Model из пакета models
# Далее описываем поля модели и их типы
class Post(models.Model):
    
    text = models.TextField(
        max_length=400,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text