from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Team
from cars.models import Car


# Create your views here.
class Home(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        team = Team.objects.all()
        featured_cars = Car.objects.order_by('-created_at').filter(is_featured=True)
        latest_cars = Car.objects.order_by('-created_at')
        context['title'] = 'Home'
        context['team'] = team
        context['featured_cars'] = featured_cars
        context['latest_cars'] = latest_cars
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
