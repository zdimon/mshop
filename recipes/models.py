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
    author_photo  = models.ImageField(upload_to='recipe', verbose_name=u'Изображение автора', blank=True)
    ingradients = tinymce_models.HTMLField(verbose_name=u'Инградиенты')
    datetime = models.DateTimeField(u'Дата публикации')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return u"/рецепт/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Рецепты'
        app_label = u'Содержимое'
        db_table = 'recipes_recipe'

class RecipesSteps(models.Model):
    recipe = models.ForeignKey('Recipe')
    title = models.CharField(max_length=250, verbose_name=u'Заголовок', blank=True)
    image  = models.ImageField(upload_to='recipe',verbose_name=u'Изображение')
    desc = models.TextField(verbose_name=u'Описание', blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = u'Шаги'
        ordering = ['id']
        app_label = u'Содержимое'
        db_table = 'recipes_recipessteps'

class RecipesComments(models.Model):
    recipe = models.ForeignKey('Recipe')
    author = models.CharField(max_length=250, verbose_name=u'Автор')
    comment = models.TextField(verbose_name=u'Текст')
    is_pub = models.BooleanField(default=False, verbose_name=u'Опубликовано')
    datetime = models.DateTimeField(u'Дата публикации')
    def __unicode__(self):
        return self.author
    class Meta:
        verbose_name_plural = u'Комментарии'
        app_label = u'Содержимое'
        db_table = 'recipes_recipescomments'

