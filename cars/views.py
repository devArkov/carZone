from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Car


# Create your views here.
class Cars(ListView):
    model = Car
    template_name = 'pages/cars.html'
    context_object_name = 'cars'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Cars'
        return context


def search(request):
    cars = Car.objects.order_by('-created_at')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    return render(request, 'pages/search.html', {'cars': cars})
