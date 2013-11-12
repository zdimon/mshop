#-*- coding: utf-8 -*-
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from mshop.models import MshopCategories
from mshop.models import MshopGoods
from mshop.models import MshopGoodsPositions
from django.shortcuts import redirect, render_to_response
from mshop.forms import BasketForm
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def basket_show(request):
    context = {}
    bas_ses = request.session.get('basket_good')
    cnt_ses = request.session.get('basket_count')
    bas = []
    for b in bas_ses:
        try:
            t = MshopGoodsPositions.objects.get(pk=b)
            indx = bas_ses.index(b)
            t.cnt = cnt_ses[indx]
            bas.append(t)
        except MshopGoodsPositions.DoesNotExist:
            return None
    context['basket'] = bas
    form = BasketForm()
    # Сохранение формы

    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            request.session['alert'] = u'Запись сохранена'
            form.save(request.POST)

    context['form'] = form
    return render_to_response('basket_show.html', context, RequestContext(request))

def basket_clear(request):
    request.session['basket_good'] = []
    request.session['basket_count'] = []
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def good_put(request,id):
    p = MshopGoodsPositions.objects.get(pk=id)

    if not 'basket_good' in request.session:
        request.session['basket_good'] = []
    if not 'basket_count' in request.session:
        request.session['basket_count'] = []


    sbb = request.session['basket_good']
    sbc = request.session['basket_count']

    if not int(id) in sbb:
        sbb.append(int(id))
        sbc.append(1)
    else:
        indx = sbb.index(int(id))
        tmp = sbc[indx]
        tmp = tmp + 1
        sbc[indx] = tmp

    request.session['basket_good'] = sbb
    request.session['basket_count'] = sbc


    #response = HttpResponse( 'blah' )
    #response.set_cookie( 'basket', 'ffffffffffffffffffffffff' )
    return redirect(p.good)

def basket_pop(request,id):
    sbg = request.session['basket_good']
    sbc = request.session['basket_count']
    if int(id) in sbg:
        indx = sbg.index(int(id))
        i = sbc.pop(int(indx))
        i = sbg.pop(int(indx))
        request.session['basket_good'] = sbg
        request.session['basket_count'] = sbc
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
