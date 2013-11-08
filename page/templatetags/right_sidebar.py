#-*- coding: utf-8 -*-
from django import template
from mshop.models import MshopCategories
from mshop.models import MshopGoodsPositions

# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон right_sidebar.html
@register.inclusion_tag("right_sidebar.html", takes_context = True)
def show_sidebar(context):
    cats = MshopCategories.objects.all() # выбираем все теги
    # возвращаем наши объекты в шаблон
    request = context['request']
    bas = []
    if 'basket_good' in request.session:
        for b in request.session['basket_good']:
            try:
                t = MshopGoodsPositions.objects.get(pk=b)
                bas.append(t)
            except MshopGoodsPositions.DoesNotExist:
               return None


    return {'cats': cats, 'basket_good': bas}

