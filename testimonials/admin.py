from django.contrib import admin
from testimonials.models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('datetime','title','content','is_pub')
    list_editable = ('is_pub',)

admin.site.register(Testimonials, TestimonialsAdmin)