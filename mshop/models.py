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
        verbose_name_plural = u'Категории товаров'
        verbose_name = u'Категорию товаров'
        app_label = u'Магазин'
        db_table = 'mshop_mshopcategories'

class MshopGoods(models.Model):
    TYPE_MESURE = (
        (u'кг.', u'кг.'),
        (u'шт.', u'шт.'),
        (u'дес.', u'дес.'),
        (u'л.', u'л.'),
        (u'100гр.', u'100гр.'),
    )

    TYPE_AMMOUNT = (
        (u'много', u'много'),
        (u'достаточно', u'достаточно'),
        (u'мало', u'мало'),
        (u'нет', u'нет'),
    )
    ammount = models.CharField(verbose_name=u'Количество',
                                    choices=TYPE_AMMOUNT,
                                    default=u'достаточно',
                                    max_length=12)

    masure = models.CharField(verbose_name=u'Единицы измерения',
                                    choices=TYPE_MESURE,
                                    default='кг.',
                                    max_length=10)
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
        app_label = u'Магазин'
        db_table = 'mshop_mshopgoods'

class MshopGoodsPositions(models.Model):
    good = models.ForeignKey(MshopGoods)
    name = models.CharField(max_length=250, verbose_name=u"Наименование")
    descr = models.CharField(max_length=250, verbose_name=u"Доп. характеристики", blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Стоимость (руб)")
    class Meta:
        verbose_name_plural = u'Позиции товаров'
        app_label = u'Содержимое'
        db_table = 'mshop_mshopgoodspositions'



class MshopBasket(models.Model):

    TYPE_CHOICES = (
        (u'Новый', u'Новый'),
        (u'Оплачен', u'Оплачен'),
        (u'Доставка', u'Доставка'),
        (u'Доставлен', u'Доставлен'),
        (u'Отказ', u'Отказ'),
    )
    basket_type = models.CharField(verbose_name=u'Статус заказа',
                                    choices=TYPE_CHOICES,
                                    default=u'Новый',
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

    @property
    def cost(self):
        r = 0
        pos = MshopBasketPositions.objects.all().filter(basket_id=self.id)
        #import pdb; pdb.set_trace()
        for i in pos:
            r = r + (i.position.cost*i.ammount)
        return r

    class Meta:
        verbose_name_plural = u'Заказы'
        verbose_name = u'заказ'
        app_label = u'Магазин'
        db_table = 'mshop_mshopbasket'

class MshopBasketPositions(models.Model):
    position = models.ForeignKey('MshopGoodsPositions')
    basket = models.ForeignKey('MshopBasket', default=False)
    ammount = models.IntegerField(verbose_name=u'Количество', blank=False)
    class Meta:
        verbose_name_plural = u'Позиции корзины'
        app_label = u'Содержимое'
        db_table = 'mshop_mshopbasketpositions'

class MshopGoodsComments(models.Model):
    recipe = models.ForeignKey('MshopGoods')
    author = models.CharField(max_length=250, verbose_name=u'Автор', blank=False)
    comment = models.TextField(verbose_name=u'Текст', blank=False)
    is_pub = models.BooleanField(default=False)
    datetime = models.DateTimeField(u'Дата публикации')
    class Meta:
        verbose_name_plural = u'Комментарии'
        app_label = u'Содержимое'
        db_table = 'mshop_mshopgoodscomments'