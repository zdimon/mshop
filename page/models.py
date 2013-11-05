# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    short_content =   models.TextField(verbose_name=u'Короткое описание',blank=True)
    content =tinymce_models.HTMLField(verbose_name=u'Содержимое')
    seo_content = models.TextField(verbose_name=u'МЕТА содержимое')
    seo_title =   models.TextField(verbose_name=u'МЕТА заголовок')

    seo_keywords = models.TextField(verbose_name=u'МЕТА keywords')
    slug = models.CharField(max_length=250, verbose_name=u'Идентификатор',blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = u'Страницы'

# Create your models here.
