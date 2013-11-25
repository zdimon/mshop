# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News
from news.models import NewsImages
#from sorl.thumbnail.admin import AdminImageMixin


from django.forms import ModelForm
from utils.admin_image_widjet import AdminImageWidget



class NewsImageForm(ModelForm):
    """
    Image Admin Form
    """
    class Meta:
        model = NewsImages
        widgets = {
            'image' : AdminImageWidget,
        }

class NewsForm(ModelForm):
    class Meta:
        model = News
        widgets = {
            'image' : AdminImageWidget,
        }


class NewsImagesInline(admin.TabularInline):

#class NewsImagesInline(AdminImageMixin, admin.TabularInline):

    model = NewsImages
    verbose_name_plural = u'Изображения'
    form = NewsImageForm


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        NewsImagesInline,
    ]
    form = NewsForm
    list_display = ['title','desc','thumb', 'pub']
    actions = ['make_published']

    def make_published(self, request, queryset):
        for obj in queryset:
            if obj.pub:
                obj.pub = False
            else:
                obj.pub = True
            obj.save()
    make_published.short_description = u"Опубликовать/скрыть выбранные записи"


admin.site.register(News, NewsAdmin)
