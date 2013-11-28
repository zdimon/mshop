# -*- coding: utf-8 -*-
from django.contrib import admin
from mshop.models import MshopCategories
from mshop.models import MshopGoods
from mshop.models import MshopGoodsPositions
from mshop.models import MshopBasket
from mshop.models import MshopBasketPositions
from mshop.models import MshopGoodsComments

class MshopCategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(MshopCategories, MshopCategoriesAdmin)


class MshopGoodsPositionsInline(admin.TabularInline):
    model = MshopGoodsPositions
    verbose_name_plural = u'Товарные позиции'
    verbose_name = u'товарную позицию'


class MshopGoodsAdmin(admin.ModelAdmin):
    inlines = [
        MshopGoodsPositionsInline,
    ]
    list_display = ('thumbnail','name','category','ammount')
    list_display_links = ('thumbnail','name')
    list_filter = ('category__name',)
    list_editable = ('ammount',)
admin.site.register(MshopGoods, MshopGoodsAdmin)


class MshopBasketAdmin(admin.ModelAdmin):
    pass

admin.site.register(MshopBasket, MshopBasketAdmin)


class MshopGoodsCommentsAdmin(admin.ModelAdmin):
    list_display = ['author','comment', 'is_pub', 'good', 'created_at']
    actions = ['make_published']

    def make_published(self, request, queryset):
        for obj in queryset:
            if obj.is_pub:
                obj.is_pub = False
            else:
                obj.is_pub = True
            obj.save()
    make_published.short_description = u"Опубликовать/скрыть выбранные записи"


admin.site.register(MshopGoodsComments, MshopGoodsCommentsAdmin)
