from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Team


# Create your views here.
class Home(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        team = Team.objects.all()
        context['title'] = 'Home'
        context['team'] = team
        return context


class About(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        team = Team.objects.all()
        context['title'] = 'About'
        context['team'] = team
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
