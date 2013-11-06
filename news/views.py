from django.http import HttpResponse
from django.template import loader, RequestContext
from news.models import News

def news_list(request):
    items = News.objects.all()
    t = loader.get_template('recipes_list.html')
    c = RequestContext(request,{'items': items})
    return HttpResponse(t.render(c))

def news_item(request,id):
    item = News.objects.get(pk=id)
    t = loader.get_template('recipes_item.html')
    c = RequestContext(request,{'item': item})
    return HttpResponse(t.render(c))