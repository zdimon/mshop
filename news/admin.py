# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News
from news.models import NewsImages
from sorl.thumbnail.admin import AdminImageMixin


class NewsImagesInline(AdminImageMixin, admin.TabularInline):
    model = NewsImages
    verbose_name_plural = u'Изображения'


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        NewsImagesInline,
    ]




admin.site.register(News, NewsAdmin)
