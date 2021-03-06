# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from recipes.views import RecipesView
from mshop.views import OrdersView
from django.contrib.auth.models import Group
from news.views import news_list

admin.autodiscover()
admin.site.unregister(Group)

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'page.views.home', name='home'),
     url(ur'^о-нас$', 'page.views.page_show', {'slug': 'about_us'}, name='about_us'),
     url(ur'^доставка$', 'page.views.page_show', {'slug': 'delivery'}, name='delivery'),
     url(ur'^гарантия-качества$', 'page.views.page_show', {'slug': 'quality'}, name='quality'),

    # url(r'^settings/', include('settings.foo.urls')),

    # контактная форма ############
    url(ur'^контакты$', 'just_contact.views.index', name='just_contact'),
    ##################

    # новости############
    url(ur'^ферма/новости$', news_list.as_view(), name='news_list'),
    url(ur'^новость/(?P<id>\d+)/$', 'news.views.news_item'),
    ##################

    #####Рецепты####################
    #url(ur'^ферма/рецепты$', 'recipes.views.recipes_list', name='recipes_list'),
    url(ur'^ферма/рецепты$', RecipesView.as_view(), name='recipes_list'),
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
    url(ur'^ферма/продукты$','mshop.views.products_list',name='products_list'),
    url(ur'^каталог/(?P<id>\d+)/$', 'mshop.views.category_show', name='category_show'),
    url(ur'^товар/(?P<id>\d+)/$', 'mshop.views.good_show', name='good_show'),
    url(ur'^в-корзину/(?P<id>\d+)/$', 'mshop.views.good_put', name='good_put'),
    url(ur'^моя-корзина/$', 'mshop.views.basket_show', name='basket_show'),
    url(ur'^мои-заказы/$', OrdersView.as_view(), name='orders_list'),
    url(ur'^очистить-корзинку/$', 'mshop.views.basket_clear', name='basket_clear'),
    url(ur'^удалить-из-корзинки/(?P<id>\d+)/$', 'mshop.views.basket_pop', name='basket_pop'),
    url(ur'^заказ/(?P<id>\d+)/$', 'mshop.views.order_show', name='order_show'),
    url(ur'^подтвердить-заказ/(?P<id>\d+)/$', 'mshop.views.order_confirm', name='order_confirm'),
    url(ur'^удалить-заказ/(?P<id>\d+)/$', 'mshop.views.order_delete', name='order_delete'),
    #####################################

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^tinymce/', include('tinymce.urls')),
     url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )