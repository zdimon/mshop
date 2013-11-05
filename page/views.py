#-*- coding: utf-8 -*-
from page.models import Page
from django.template import loader, RequestContext
from django.http import HttpResponse


def page_show(request,slug):
    page = Page.objects.get(slug=slug)
    t = loader.get_template('show.html')
    c = RequestContext(request,{'page':page, 'slug': slug})
    return HttpResponse(t.render(c))

def home(request):
    t = loader.get_template('homepage.html')
    c = RequestContext(request,{})
    return HttpResponse(t.render(c))