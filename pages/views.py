from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Home'
        return context


class Cars(TemplateView):
    template_name = 'pages/cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Cars'
        return context


class About(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'About'
        return context


class Services(TemplateView):
    template_name = 'pages/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Services'
        return context


class Contact(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Contact'
        return context
