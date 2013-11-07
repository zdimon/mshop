#-*- coding: utf-8 -*-
from page.models import Page
from django.template import loader, RequestContext
from django.http import HttpResponse
from mshop.models import MshopCategories
from recipes.models import Recipe

def page_show(request,slug):
    page = Page.objects.get(slug=slug)
    t = loader.get_template('show.html')
    c = RequestContext(request,{'page':page, 'slug': slug})
    return HttpResponse(t.render(c))

def home(request):
    categories =  MshopCategories.objects.all()
    recepies = Recipe.objects.all()
    t = loader.get_template('homepage.html')
    c = RequestContext(request,{'categories': categories, 'recepies': recepies})
    return HttpResponse(t.render(c))