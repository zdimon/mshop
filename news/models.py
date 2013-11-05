# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
from news.items import ThumbnailImageField

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = ThumbnailImageField(upload_to='news', verbose_name=u'Изображение', blank=True)
    desc = models.TextField(verbose_name=u'Короткое описание')
    content =tinymce_models.HTMLField()
    datetime = models.DateTimeField(u'Дата публикации')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return u"/новость/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Новости'

class NewsImages(models.Model):
    news = models.ForeignKey('News')
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = ThumbnailImageField(upload_to='recipe',verbose_name=u'Изображение')
    alias = models.CharField(max_length=250, verbose_name=u'Метка')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = u'Изображения к новостям'
