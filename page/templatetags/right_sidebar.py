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
    sgood = request.session['basket_good']
    scount = request.session['basket_count']
    if 'basket_good' in request.session:
        for b in request.session['basket_good']:
            try:
                t = MshopGoodsPositions.objects.get(pk=b)
            except MshopGoodsPositions.DoesNotExist:
                return None
            else:
                indx = int(sgood.index(b))
                try:
                     i = scount[indx]
                except IndexError:
                    request.session['basket_good'] = []
                    request.session['basket_count'] = []
                    return {'cats': cats, 'basket_good': bas}
                else:
                     t.cnt = i
            bas.append(t)


    return {'cats': cats, 'basket_good': bas}

