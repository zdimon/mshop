# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

class Testimonials(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = tinymce_models.HTMLField()
    is_pub = models.BooleanField(default=False, verbose_name=u'Опубликовано?')
    class Meta:
        verbose_name_plural = u'Отзывы'
        verbose_name =  u'отзыв'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/отзыв/%i/" % self.id
