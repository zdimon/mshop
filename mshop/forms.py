# -*- coding: utf-8 -*-

from django import  forms
from mshop.models import MshopBasket, MshopBasketPositions, MshopGoodsPositions
from django.contrib.auth.models import User
from django.contrib import auth
from registrations.models import RegistrationProfile
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


