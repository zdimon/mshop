# -*- coding: utf-8 -*-
from testimonials.models import Testimonials
from django.views.generic import ListView, DetailView

class TestimonialsListView(ListView): # представление в виде списка
    model = Testimonials                   # модель для представления

class TestimonialsDetailView(DetailView): # детализированное представление модели
    model = Testimonials

