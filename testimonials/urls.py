#coding: utf-8
from django.conf.urls import patterns, url

from testimonials.views import TestimonialsListView, TestimonialsDetailView

urlpatterns = patterns('',
url(r'^$', TestimonialsListView.as_view(template_name='list.html'), name='testimonials_list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', TestimonialsDetailView.as_view(template_name='detail.html')), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

)
