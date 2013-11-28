# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
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
                                    default=u'кг.',
                                    max_length=10)
    category = models.ForeignKey('MshopCategories')
    name = models.CharField(max_length=250, verbose_name=u"Наименование", blank=False)
    image  = models.ImageField(upload_to='goods', verbose_name=u'Изображение', blank=True)
    description = tinymce_models.HTMLField()
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return u"/товар/%i/" % self.id
    @property
    def thumbnail(self):
        if (self.image):
            image = get_thumbnail(self.image.path, '40x40', crop='center', format='PNG')
            return mark_safe(u'<img src="%s" />' % image.url)
        return u'нет изображения'
    class Meta:
        verbose_name_plural = u'Товары'
        verbose_name = u'товар'


class MshopGoodsPositions(models.Model):
    good = models.ForeignKey('MshopGoods')
    name = models.CharField(max_length=250, verbose_name=u"Наименование")
    descr = models.CharField(max_length=250, verbose_name=u"Доп. характеристики", blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Стоимость (руб)")
    class Meta:
        verbose_name_plural = u'Позиции товаров'



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

    def send_notification(self):

        from utils.mail import send_mail, render_template
        from settings.settings import EMAIL_ADMIN, PROJECT_PATH
        sa = 0
        out =u'<tr>'
        for o in self.mshopbasketpositions_set.all():
            s = o.ammount*o.position.cost
            out += u'<td>'+unicode(o.position.good)+u'<td>'
            out += u'<td>'+unicode(o.position.cost)+u'руб/'+unicode(o.position.good.masure)+u'<td>'
            out += u'<td>'+unicode(o.ammount)+u' '+unicode(o.position.good.masure)+u'<td>'
            out += u'<td>'+unicode(s)+u'<td>'
            sa += s
        out += '</tr>'

        t = render_template('order.txt',{
            'email':self.email,
            'name':self.name,
            'address':self.address,
            'desc':self.description,
            'city':self.city,
            'phone': self.phone,
            'order': out,
            'total': sa
        })
        send_mail(EMAIL_ADMIN,EMAIL_ADMIN,u'Поступил новый заказ!',t)

    class Meta:
        verbose_name_plural = u'Заказы'
        verbose_name = u'заказ'


class MshopBasketPositions(models.Model):
    position = models.ForeignKey('MshopGoodsPositions')
    basket = models.ForeignKey('MshopBasket', default=False)
    ammount = models.IntegerField(verbose_name=u'Количество', blank=False)
    class Meta:
        verbose_name_plural = u'Позиции корзины'


class MshopGoodsComments(models.Model):
    good = models.ForeignKey('MshopGoods')
    author = models.CharField(max_length=250, verbose_name=u'Автор', blank=False)
    comment = models.TextField(verbose_name=u'Текст', blank=False)
    is_pub = models.BooleanField(default=False,verbose_name=u'Опубликован')
    created_at = models.DateField(u'Дата публикации',auto_now_add=True)
    class Meta:
        verbose_name_plural = u'Отзывы (продукты)'
