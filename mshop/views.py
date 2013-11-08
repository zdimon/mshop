#-*- coding: utf-8 -*-
from django.template import loader, RequestContext
from django.http import HttpResponse
from mshop.models import MshopCategories
from mshop.models import MshopGoods
from mshop.models import MshopGoodsPositions
from django.shortcuts import redirect


def category_list(request):
    categories = MshopCategories.objects.all()
    t = loader.get_template('category_list.html')
    c = RequestContext(request,{'categories': categories})
    return HttpResponse(t.render(c))


def category_show(request,id):
    category = MshopCategories.objects.get(pk=id)
    goods = MshopGoods.objects.all().filter(category_id=id)
    t = loader.get_template('category_show.html')
    c = RequestContext(request,{'category':category, 'goods':goods})
    return HttpResponse(t.render(c))


def good_show(request,id):
    good = MshopGoods.objects.get(pk=id)
    t = loader.get_template('good_show.html')
    c = RequestContext(request,{ 'good':good, 'basket': request.session.get('basket_good') })
    return HttpResponse(t.render(c))


def good_put(request,id):
    p = MshopGoodsPositions.objects.get(pk=id)

    if not 'basket_good' in request.session:
        request.session['basket_good'] = []
    else:
        sbb = request.session['basket_good']
        sbb.append(int(id))
        request.session['basket_good'] = sbb

  

    #response = HttpResponse( 'blah' )
    #response.set_cookie( 'basket', 'ffffffffffffffffffffffff' )
    return redirect(p.good)
