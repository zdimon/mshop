# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

class Testimonials(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Ваше имя') # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации', auto_now_add=True) # дата публикации
    content = tinymce_models.HTMLField(verbose_name=u'Сообщение')
    is_pub = models.BooleanField(default=False, verbose_name=u'Опубликовано?')
    class Meta:
        verbose_name_plural = u'Отзывы'
        verbose_name =  u'отзыв'
        app_label = u'Содержимое'
        db_table = 'testimonials_testimonials'
        ordering = ['-id']
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/testimonials/%i/" % self.id
