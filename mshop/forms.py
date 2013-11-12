# -*- coding: utf-8 -*-

from django import  forms
from mshop.models import MshopBasket, MshopBasketPositions


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
        import pdb; pdb.set_trace()
        b = MshopBasket.objects.create(
            phone = data['phone'],
            name  = data['name'],
            address = data ['address']
        )


        c = RecipesComments.objects.create(
           author = data['name'],
           comment = data['message'],
           recipe_id = data['recipe_id'],
           datetime = datetime.date.today()
        )
        c.save()