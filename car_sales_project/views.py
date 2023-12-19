import django.db
from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from cars.models import CarModel
from brands.models import BrandModel
from user.models import Purchase
from django.shortcuts import get_object_or_404



def home(request, category_slug=None):
    cars = CarModel.objects.all()
    all_brands = BrandModel.objects.all()
    total_cars = CarModel.objects.all().count()
    if category_slug:
        brand = BrandModel.objects.filter(slug=category_slug).first()
        if brand:
            cars = CarModel.objects.filter(brand=brand)

    return render(request, 'home.html', {'cars': cars, 'all_brands': all_brands, 'total_cars' : total_cars})


    
class ShowDetails(DetailView):
    model = CarModel
    template_name = 'details.html'
    context_object_name = 'car'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_car = self.get_object()
        current_brand = current_car.brand
        total_cars_found = CarModel.objects.filter(brand=current_brand).count()

        context['total_cars_found'] = total_cars_found
        return context
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         car = self.get_object()
    #         Purchase.objects.create(user=request.user, car=car)
            
    #         current_brand = car.brand
    #         total_cars_found = CarModel.objects.filter(brand=current_brand).exclude(pk=car.pk).count()

    #         if total_cars_found > 0:
    #             # Update the count
    #             car_to_update = get_object_or_404(CarModel, pk=car.pk)
    #             car_to_update.available_quantity = total_cars_found
    #             car_to_update.save()
            
            

    