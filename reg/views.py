from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import redirect

def logout(request):
    #if not request.user.is_authenticated():
    logout(request)
    return redirect('/')

def welcome(request):
    t = loader.get_template('welcome.html')
    return HttpResponse(t.render(c))