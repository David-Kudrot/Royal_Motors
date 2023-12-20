import django.db
from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from cars.models import CarModel
from brands.models import BrandModel
from user.models import Purchase
from django.shortcuts import get_object_or_404
from cars.forms import CommentForm



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
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # current_car = self.get_object()
        # current_brand = current_car.brand
        # total_cars_found = CarModel.objects.filter(brand=current_brand).count()

        # context['total_cars_found'] = total_cars_found
        # return context
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
        
            
            

    