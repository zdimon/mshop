from django.contrib import admin
from testimonials.models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Testimonials, TestimonialsAdmin)