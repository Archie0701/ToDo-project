from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок', )  # Заголовок задачи
    description = models.TextField(blank=True, null=True, verbose_name='Описание', )  # Описание задачи (необязательно)
    completed = models.BooleanField(default=False, verbose_name='Выполнена', )  # Выполнена или нет
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", )  # Дата создания
    due_date = models.DateField(blank=True, null=True, verbose_name='Срок выполнения', )  # Срок выполнения (необязательно)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', )  # Пользователь-владелец задачи

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Задача'
        verbose_name_plural='Задачи'