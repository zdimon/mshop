# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = models.ImageField(upload_to='recipe',verbose_name=u'Изображение',blank=True)
    desc = tinymce_models.HTMLField(verbose_name=u'Описание')
    time = models.CharField(verbose_name=u'Время приготовления',max_length=250)
    authors = tinymce_models.HTMLField(verbose_name=u'Авторы')
    ingradients = tinymce_models.HTMLField(verbose_name=u'Инградиенты')
    datetime = models.DateTimeField(u'Дата публикации')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return u"/рецепт/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Рецепты'

class RecipesSteps(models.Model):
    recipe = models.ForeignKey('Recipe')
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = models.ImageField(upload_to='recipe',verbose_name=u'Изображение')
    desc = models.TextField(verbose_name=u'Описание')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = u'Шаги'
        ordering = ['id']

class RecipesComments(models.Model):
    recipe = models.ForeignKey('Recipe')
    author = models.CharField(max_length=250, verbose_name=u'Автор')
    comment = models.TextField(verbose_name=u'Текст')
    is_pub = models.BooleanField(default=False)
    datetime = models.DateTimeField(u'Дата публикации')
    class Meta:
        verbose_name_plural = u'Комментарии'