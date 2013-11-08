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

    # url(r'^settings/', include('settings.foo.urls')),

    # новости############
    url(ur'^ферма/новости$', 'news.views.news_list', name='news_list'),
    url(ur'^новость/(?P<id>\d+)/$', 'news.views.news_item'),
    ##################

    #####Рецепты####################
    url(ur'^ферма/рецепты$', 'recipes.views.recipes_list', name='recipes_list'),
    url(ur'^рецепт/(?P<id>\d+)/$', 'recipes.views.recipes_item', name='recipes_item'),
    ####################

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login_form'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    url(ur'^accounts/profile/$', 'reg.views.welcome'),

    url(r'^accounts/', include('registrations.backends.default.urls')),

    url(ur'^contact/', include('contact_form.urls')),

    url(r'^testimonials/', include('testimonials.urls')),

    url(r'^captcha/', include('captcha.urls')),

    #######Магазин#####################
     url(ur'^наша/продукция$','mshop.views.category_list',name='category_list'),
    url(ur'^каталог/(?P<id>\d+)/$', 'mshop.views.category_show', name='category_show'),
    url(ur'^товар/(?P<id>\d+)/$', 'mshop.views.good_show', name='good_show'),
    url(ur'^в-корзину/(?P<id>\d+)/$', 'mshop.views.good_put', name='good_put'),
    #####################################

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

