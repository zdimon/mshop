# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
# Create your models here.

# Create your models here.
class MshopCategories(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Название', blank=False)
    image  = models.ImageField(upload_to='mshop_categories', verbose_name=u'Изображение', blank=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return u"/каталог/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Категории продуктов'
        verbose_name = u'Категорию продуктов'


class MshopGoods(models.Model):
    TYPE_MESURE = (
        (u'кг.', u'кг.'),
        (u'шт.', u'шт.'),
    )
    masure = models.CharField(verbose_name=u'Единицы измерения',
                                    choices=TYPE_MESURE,
                                    default='кг.',
                                    max_length=6)
    category = models.ForeignKey('MshopCategories')
    name = models.CharField(max_length=250, verbose_name=u"Наименование", blank=False)
    image  = models.ImageField(upload_to='goods', verbose_name=u'Изображение', blank=True)
    description = tinymce_models.HTMLField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return u"/товар/%i/" % self.id
    class Meta:
        verbose_name_plural = u'Товары'
        verbose_name = u'товар'

class MshopGoodsPositions(models.Model):
    good = models.ForeignKey(MshopGoods)
    name = models.CharField(max_length=250, verbose_name=u"Наименование")
    descr = models.CharField(max_length=250, verbose_name=u"Доп. характеристики", blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Стоимость (руб)")




class MshopBasket(models.Model):

    TYPE_CHOICES = (
        ('new', u'Новый'),
        ('paid', u'Оплачен'),
        ('onway', u'Доставка'),
        ('done', u'Доставлен'),
        ('rejected', u'Отказ'),
    )
    basket_type = models.CharField(verbose_name=u'Статус заказа',
                                    choices=TYPE_CHOICES,
                                    default='new',
                                    max_length=10)
    session = models.CharField(max_length=250, verbose_name=u'Сессия', blank=True)

    phone = models.CharField(max_length=250, verbose_name=u'Телефон', blank=False)
    name = models.CharField(max_length=250, verbose_name=u'Имя' , blank=False)
    address = models.CharField(max_length=250, verbose_name=u'Адресс', blank=False)

    description = models.TextField(blank=True, default=False)
    city = models.CharField(max_length=250, verbose_name=u'Город', blank=False, default=False)
    email = models.EmailField(verbose_name=u'Email', blank=False, default=False)
    user = models.IntegerField(default=False)

    datetime = models.DateField(auto_now_add=True)
    def get_absolute_url(self):
        return u"/заказ/%i/" % self.id
    def __unicode__(self):
        return self.phone
    class Meta:
        verbose_name_plural = u'Заказы'
        verbose_name = u'заказ'

class MshopBasketPositions(models.Model):
    position = models.ForeignKey('MshopGoodsPositions')
    basket = models.ForeignKey('MshopBasket')
    ammount = models.IntegerField(verbose_name=u'Количество', blank=False)


class RecipesComments(models.Model):
    recipe = models.ForeignKey('MshopGoods')
    author = models.CharField(max_length=250, verbose_name=u'Автор', blank=False)
    comment = models.TextField(verbose_name=u'Текст', blank=False)
    is_pub = models.BooleanField(default=False)
    datetime = models.DateTimeField(u'Дата публикации')
    class Meta:
        verbose_name_plural = u'Комментарии'