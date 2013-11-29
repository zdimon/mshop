from django.http import HttpResponse
from django.template import loader, RequestContext
from news.models import News
from django.views.generic import ListView

class news_list(ListView):
    queryset = News.objects.all().order_by('-id')
    template_name = 'news_list.html'
    paginate_by = 8


#def news_list(request):
#    items = News.objects.all()
#    t = loader.get_template('news_list.html')
#    c = RequestContext(request,{'items': items})
#    return HttpResponse(t.render(c))

def news_item(request,id):
    item = News.objects.get(pk=id)
    t = loader.get_template('news_item.html')
    c = RequestContext(request,{'item': item})
    return HttpResponse(t.render(c))