from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def send_mail(address_to,address_from,subject,html_content):
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, address_from, [address_to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def render_template(tpl,dict={}):
    return render_to_string(tpl,dict)
