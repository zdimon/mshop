#coding: utf-8
from django.conf.urls import patterns, url

from testimonials.views import TestimonialsListView, TestimonialsDetailView, TestimonialsCreateView

urlpatterns = patterns('',
url(r'^$', TestimonialsListView.as_view(template_name='list.html'), name='testimonials_list'),
url(r'^(?P<pk>\d+)/$', TestimonialsDetailView.as_view(template_name='detail.html')),
url(r'^new$', TestimonialsCreateView.as_view(template_name='new.html'), name='testimonials_create'),

)
