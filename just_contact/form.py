#coding: utf-8
from django import forms
from captcha.fields import CaptchaField
from django.core.mail import EmailMultiAlternatives
from settings.settings import EMAIL_ADMIN

class JustContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'20'}), max_length=100, label='Имя',required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'20'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':60}), label='Сообщение',required=True)
    captcha = CaptchaField()
    def save(self):
        data = self.cleaned_data


        subject, from_email, to = u'Поступило сообщение из контактной формы', data['email'], [EMAIL_ADMIN]
        text_content = u'Имя:'+data['name']+u' Email: '+data['email']+u' Сообщение:'+data['body']
        html_content = u'<b>Имя:</b>'+data['name']+u'<br/>'+u'<b>Email:</b>'+data['email']+u'<b>Сообщение:</b>'+data['body']
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        #body = u'<b>Имя:</b>'+data['name']+u'<br/>'+u'<b>Email:</b>'+data['email']+u'<b>Сообщение:</b>'+data['body']
        #send_mail(u'Поступило сообщение из контактной формы', body, data['email'], [EMAIL_ADMIN])
