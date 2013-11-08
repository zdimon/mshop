# -*- coding: utf-8 -*-


from django import  forms


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