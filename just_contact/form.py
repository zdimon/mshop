#coding: utf-8
from django import forms
from captcha.fields import CaptchaField
from django.core.mail import send_mail
from settings.settings import EMAIL_ADMIN

class JustContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'20'}), max_length=100, label='Имя',required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'20'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':60}), label='Сообщение',required=True)
    captcha = CaptchaField()
    def save(self):
        data = self.cleaned_data
        body = u'<b>Имя:</b>'+data['name']+u'<br/>'+u'<b>Email:</b>'+data['email']+u'<b>Сообщение:</b>'+data['body']
        send_mail(u'Поступило сообщение из контактной формы', body, data['email'], [EMAIL_ADMIN])
