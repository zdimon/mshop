# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Create your models here.
class MshopCategories(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Название')
    image  = models.ImageField(upload_to='mshop_categories', verbose_name=u'Изображение', blank=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return u"/продукты/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Категории продуктов'
        verbose_name = u'Категорию продуктов'
