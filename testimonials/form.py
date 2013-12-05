#coding: utf-8
from testimonials.models import Testimonials
from django import forms

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        exclude = ('is_pub', 'datetime')
    def save(self):
        from utils.mail import send_mail
        from settings.settings import EMAIL_ADMIN
        data = self.cleaned_data
        subject = u'Поступил новый отзыв от посетителя', data['title']
        html_content = data['content']
        send_mail(EMAIL_ADMIN,EMAIL_ADMIN,subject,html_content)
        return super(TestimonialsForm,self).save()
