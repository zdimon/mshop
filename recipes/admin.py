# -*- coding: utf-8 -*-
from django.contrib import admin
from recipes.models import Recipe
from recipes.models import RecipesSteps
from recipes.models import RecipesComments

class RecipesStepsInline(admin.TabularInline):
    model = RecipesSteps
    verbose_name_plural = u'Шаги'

class RecipesCommentsInline(admin.TabularInline):
    model = RecipesComments
    verbose_name_plural = u'Комментарии'

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipesStepsInline,
        RecipesCommentsInline,
    ]




admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipesSteps)
admin.site.register(RecipesComments)
