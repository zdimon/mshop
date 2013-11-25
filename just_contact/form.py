#coding: utf-8
from django import forms
from captcha.fields import CaptchaField
from settings.settings import EMAIL_ADMIN
from utils.mail import send_mail, render_template

class JustContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'20'}), max_length=100, label='Имя',required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':'20'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':60}), label='Сообщение',required=True)
    captcha = CaptchaField()
    def save(self):
        data = self.cleaned_data
        subject, from_email, to = u'Поступило сообщение из контактной формы', data['email'], EMAIL_ADMIN
        html_content = render_template('message.txt',{'email':data['email'], 'name': data['name'], 'message':data['body']})
        send_mail(to,from_email,subject,html_content)