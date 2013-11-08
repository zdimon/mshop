# -*- coding: utf-8 -*-
from django.contrib import admin
from mshop.models import MshopCategories
from mshop.models import MshopGoods
from mshop.models import MshopGoodsPositions
from mshop.models import MshopBasket
from mshop.models import MshopBasketPositions
from mshop.models import RecipesComments

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

admin.site.register(MshopGoods, MshopGoodsAdmin)


class MshopBasketAdmin(admin.ModelAdmin):
    pass

admin.site.register(MshopBasket, MshopBasketAdmin)