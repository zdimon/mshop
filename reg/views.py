from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import redirect


def welcome(request):
    t = loader.get_template('welcome.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))