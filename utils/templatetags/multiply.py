from django.template import Library

register = Library()

@register.filter
def multiply(value, arg):
    i = int(arg)
    return value*i
