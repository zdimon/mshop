# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'page.views.home', name='home'),
     url(ur'^о-нас$', 'page.views.page_show', {'slug': 'about_us'}, name='about_us'),
     url(ur'^доставка$', 'page.views.page_show', {'slug': 'delivery'}, name='delivery'),
     url(ur'^гарантия-качества$', 'page.views.page_show', {'slug': 'quality'}, name='quality'),
     url(r'^list$','mshop.views.category_list',name='category_list'),
    # url(r'^settings/', include('settings.foo.urls')),
    url(ur'^ферма/новости$', 'news.views.news_list', name='news_list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

