# -*- coding: utf-8 -*-
from django.contrib import admin
from recipes.models import Recipe
from recipes.models import RecipesSteps
from recipes.models import RecipesComments
from django.forms import ModelForm
from utils.admin_image_widjet import AdminImageWidget


class RecipeStepForm(ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'image' : AdminImageWidget,
        }

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'image' : AdminImageWidget,
            'author_photo' : AdminImageWidget,
        }

class RecipesStepsInline(admin.TabularInline):
    model = RecipesSteps
    verbose_name_plural = u'Шаги'
    form = RecipeStepForm

class RecipesCommentsInline(admin.TabularInline):
    model = RecipesComments
    verbose_name_plural = u'Комментарии к рецептам'



class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipesStepsInline,
        RecipesCommentsInline,
    ]
    form = RecipeForm

class RecipesCommentAdmin(admin.ModelAdmin):
    list_display = ['author','comment', 'is_pub', 'datetime']
    actions = ['make_published']
    def make_published(self, request, queryset):
        for obj in queryset:
            if obj.is_pub:
                obj.is_pub = False
            else:
                obj.is_pub = True
            obj.save()
    make_published.short_description = u"Опубликовать/скрыть выбранные записи"


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipesComments,RecipesCommentAdmin,)
