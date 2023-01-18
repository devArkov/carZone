from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class Cars(TemplateView):
    template_name = 'pages/cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Cars'
        return context
