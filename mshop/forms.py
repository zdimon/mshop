# -*- coding: utf-8 -*-

from django import  forms
from mshop.models import MshopBasket, MshopBasketPositions, MshopGoodsPositions, MshopGoodsComments
from django.contrib.auth.models import User
from django.contrib import auth
from registrations.models import RegistrationProfile
from captcha.fields import CaptchaField
import datetime
#from django_bootstrap_wysiwyg.widgets import WysiwygInput

attrs_dict = { 'class': 'required' }


class BasketForm(forms.Form):


    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs=attrs_dict),
                           label=u'Имя')
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                             maxlength=200)),
                             label=u'Email')
    phone = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs=attrs_dict),
                           label=u'Имя')
    address = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs=attrs_dict),
                           label=u'Имя')
    city = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs=attrs_dict),
                           label=u'Имя')
    description = forms.CharField(max_length=100,
                           widget=forms.Textarea(attrs={ 'rows':5, 'cols':40 }),
                           label=u'Комментарий')

    login = forms.CharField(required=False, max_length=100,
                           widget=forms.TextInput(),
                           label=u'Логин')

    password = forms.CharField(required=False, max_length=100,
                           widget=forms.TextInput(),
                           label=u'Пароль')

    def save(self,post,request):
        data = self.cleaned_data

        b = MshopBasket.objects.create(
            phone = data['phone'],
            name  = data['name'],
            address = data ['address'],
            description = data ['description'],
            city = data ['city'],
            email = data ['email'],
        )
        ids = post.getlist('idp[]')
        idc = post.getlist('cnt[]')
        for i in ids:
            try:
                gp = MshopGoodsPositions.objects.get(pk = int(i))
            except TypeError:
                pass
            indx = ids.index(i)
            bp = MshopBasketPositions.objects.create(
                position = gp,
                ammount = idc[indx],
                basket = b,
            )
            bp.save()
        #import pdb; pdb.set_trace()
        b.save()
        if len(post['login'])>0 and len(post['password'])>0:
            user = User.objects.create_user(username=post['login'], email=post['email'],password=post['password'])
            user.save()
            user = auth.authenticate(username=post['login'], password=post['password'])
            p = RegistrationProfile.objects.create(user=user, name=post['name'], email=post['email'],city=post['city'],address=post['address'],description=post['description'],phone=post['phone'])
            p.save()
            auth.login(request, user)
        return b

class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'60'}), max_length=100, label='Имя',required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':80}), label='Сообщение',required=True)
    good_id = forms.CharField(widget=forms.HiddenInput())
    captcha = CaptchaField()
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)

    def save(self):
       data = self.cleaned_data
       import pdb; pdb.set_trace()
       c = MshopGoodsComments.objects.create(
           author = data['name'],
           comment = data['message'],
           good_id = data['good_id'],
           created_at = datetime.date.today(),
       )
       c.save()
