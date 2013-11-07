#-*- coding: utf-8 -*-
from django import template
from mshop.models import MshopCategories

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("right_sidebar.html")
def show_sidebar():
    cats = MshopCategories.objects.all() # выбираем все теги
    # возвращаем наши объекты в шаблон
    return {'cats': cats}

