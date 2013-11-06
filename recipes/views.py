from django.http import HttpResponse
from django.template import loader, RequestContext
from recipes.models import Recipe

def recipes_list(request):
    items = Recipe.objects.all()
    t = loader.get_template('recipes_list.html')
    c = RequestContext(request,{'items': items})
    return HttpResponse(t.render(c))

def recipes_item(request,id):
    item = Recipe.objects.get(pk=id)
    t = loader.get_template('recipes_item.html')
    c = RequestContext(request,{'item': item})
    return HttpResponse(t.render(c))