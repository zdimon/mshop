# -*- coding: utf-8 -*-

from django import  forms
from mshop.models import MshopBasket, MshopBasketPositions, MshopGoodsPositions


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

    def save(self,post):
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
        for i in ids:
            try:
                gp = MshopGoodsPositions.objects.get(pk = int(i))
            except: TypeError
                pass
            bp = MshopBasketPositions.objects.create(
                position = gp,
            )
            bp.save()
        import pdb; pdb.set_trace()
        b.save()


