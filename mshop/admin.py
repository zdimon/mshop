# -*- coding: utf-8 -*-
from django.contrib import admin
from mshop.models import MshopCategories


class MshopCategoriesAdmin(admin.ModelAdmin):
    pass



admin.site.register(MshopCategories, MshopCategoriesAdmin)
