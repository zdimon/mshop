#coding: utf-8
from django import forms
from recipes.models import RecipesComments
import datetime
from captcha.fields import CaptchaField

class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'60'}), max_length=100, label='Имя',required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':80}), label='Сообщение',required=True)
    recipe_id = forms.CharField(widget=forms.HiddenInput())
    captcha = CaptchaField()
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    def save(self):
       data = self.cleaned_data
       c = RecipesComments.objects.create(
           author = data['name'],
           comment = data['message'],
           recipe_id = data['recipe_id'],
           datetime = datetime.date.today()
       )
       c.save()

