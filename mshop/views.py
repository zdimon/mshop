#-*- coding: utf-8 -*-
from django.template import loader, RequestContext
from django.http import HttpResponse




def category_list(request):
    #objects = Category.objects.filter(parent_category_id=None)
    t = loader.get_template('category_list.html')
    c = RequestContext(request,{})
    return HttpResponse(t.render(c))