from django.http import HttpResponse
from django.template import loader, RequestContext
from news.models import News

def news_list(request):
    items = News.objects.all()
    t = loader.get_template('news/news_list.html')
    c = RequestContext(request,{'items':items})
    return HttpResponse(t.render(c))
