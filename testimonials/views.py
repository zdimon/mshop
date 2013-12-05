# -*- coding: utf-8 -*-
from testimonials.models import Testimonials
from django.views.generic import ListView, DetailView, CreateView
from testimonials.form import TestimonialsForm

class TestimonialsListView(ListView): # представление в виде списка
    model = Testimonials
    queryset = Testimonials.objects.all().filter(is_pub=True)

class TestimonialsDetailView(DetailView): # детализированное представление модели
    model = Testimonials

class TestimonialsCreateView(CreateView): # форма добавления
    model = Testimonials
    form_class = TestimonialsForm

    def post(self, request, *args, **kwargs):
        from django.contrib import messages
        messages.success(request, "Спасибо. Ваше сообщение сохранено и появится после проверки Администрацией.")
        return super(TestimonialsCreateView, self).post(self, request, *args, **kwargs)

    def form_valid(self, form):
        return super(TestimonialsCreateView, self).form_valid(form)
