# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
from sorl.thumbnail import get_thumbnail


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = models.ImageField(upload_to='news', verbose_name=u'Изображение', blank=True)
    desc = models.TextField(verbose_name=u'Короткое описание')
    content = tinymce_models.HTMLField()
    datetime = models.DateField(verbose_name=u'Дата публикации')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return u"/новость/%i/" % self.id

    @property
    def parsecontent(self):
        c = unicode(self.content)
        for i in self.newsimages_set.all():
            im = get_thumbnail(i.image.path, '683', crop='center', quality=99)
            istr = '<a  class="fancybox" rel="group" href="'+i.image.url+'"><img src="'+im.url+'" /></a>'
            c = c.replace(i.alias, istr)
        return c
    class Meta:
        verbose_name_plural = u'Новости'
        verbose_name = u'Новость'
        app_label = u'Содержимое'
        db_table = 'news_news'

class NewsImages(models.Model):
    news = models.ForeignKey('News')
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    image  = models.ImageField(upload_to='news', verbose_name=u'Изображение')
    alias = models.CharField(max_length=250, verbose_name=u'Метка', help_text=u'Строка которая будет заменена в тексте изображением')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = u'Изображения к новостям'
        app_label = u'Содержимое'
        db_table = 'news_newsimages'
