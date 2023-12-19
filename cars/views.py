from django.shortcuts import render
from cars.models import CarModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class CarView(CreateView):
    model = CarModel
    template_name = 'car.html'
    success_url = reverse_lazy('car')