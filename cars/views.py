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
