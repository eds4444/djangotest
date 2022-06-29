from distutils.command.upload import upload
from turtle import title, update
from django.db import models


class Women(models.Model):  #наследуем от базового класса Model (поле id прописанно автоматически в этом классе)
    title = models.CharField(max_length=250) #https://djbook.ru/rel3.0/   Модули, типы полей.
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title