from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
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
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        type_search = Car.objects.values_list('body_style', flat=True).distinct()
        context['title'] = 'Home'
        context['team'] = team
        context['featured_cars'] = featured_cars
        context['latest_cars'] = latest_cars
        context['model_search'] = model_search
        context['city_search'] = city_search
        context['year_search'] = year_search
        context['type_search'] = type_search
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


class CarDetailView(DetailView):
    model = Car
    template_name = 'pages/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Car'
        return context
