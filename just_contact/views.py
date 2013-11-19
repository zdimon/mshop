#coding: utf-8
from django.http import HttpResponse
from django.template import loader, RequestContext
from just_contact.form import JustContactForm
from django.shortcuts import render_to_response
from django.contrib import messages



def index(request):
    if request.method == 'POST':
        form = JustContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Спасибо. Ваше сообщение отправлено администрации сайта.")
            form.save()
            form = JustContactForm()
    else:
        if request.user.is_authenticated():
            form = JustContactForm(initial={'email': request.user.get_profile().email})
        else:
            form = JustContactForm()
    return render_to_response('just_contact.html', {'form':form},context_instance=RequestContext(request))