#coding: utf-8
from django.http import HttpResponse
from django.template import loader, RequestContext
from recipes.models import Recipe
from recipes.models import RecipesComments
from recipes.form import CommentForm
from django.shortcuts import render_to_response


def recipes_list(request):
    items = Recipe.objects.all()

    t = loader.get_template('recipes_list.html')
    c = RequestContext(request,{'items': items})
    return HttpResponse(t.render(c))

def recipes_item(request,id):
    pars = {}
    item = Recipe.objects.get(pk=id)
    comments = RecipesComments.objects.all().filter(recipe_id=item.pk)
    pars['item'] = item
    pars['comments'] = comments
    t = loader.get_template('recipes_item.html')
    c = RequestContext(request,{'item': item})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # ...
            pars['alert'] = u'Запись сохранена'
            form.save()
            form = CommentForm(initial={'recipe_id': item.pk})
    else:
        form = CommentForm(initial={'recipe_id': item.pk})
    pars['form'] = form
    return render_to_response('recipes_item.html', pars,context_instance=RequestContext(request))