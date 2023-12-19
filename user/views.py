from typing import Any
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views import View
from cars.models import CarModel
from user.models import Purchase
from user.forms import UpdateForm
from django.contrib.auth.views import PasswordChangeView



# Create your views here.

class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')#this will go to login page
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Email already exists')
            return self.form_invalid(form)
        else:
            form.save()
            messages.success(self.request, "Registration successful.")
            return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'Register Yourself'
        return context



class UserLoginView(LoginView):
    template_name = 'login.html'
    
    #if success_url and reverse_lazy not work then do this function
    def get_success_url(self):
        messages.success(self.request, "Logged in successful!")
        return reverse_lazy('home')
    
    def form_valid(self, form):
        # messages.success(self.request, "Logged in successful!")# eta dile log our korar time a logout message and login message ek sathe dekhabe
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Input data is invalid!")
        return super().form_invalid(form)
 

class UserProfileView(CreateView):
    template_name = "profile.html"
    def get(self, request, *args, **kwargs):
        context = Purchase.objects.filter(user=request.user)
        # print(context)
        return render(request, 'profile.html', {'context': context})  
    
    


def log_out(request):
    messages.success(request, "Logged out successfully!")
    logout(request)
    return redirect('login')


def buy_car(request, id):
    data = CarModel.objects.get(pk = id)
    qnt = data.quantity
    if qnt > 0:
        qnt -= 1
        data.quantity = qnt
        data.save()
        Purchase.objects.create(user=request.user, car = data)
        return redirect('profile')
    return render(request, 'details.html', {'car': data})


class UpdateUser(UpdateView):
    model = User
    template_name = 'register.html'
    form_class = UpdateForm
    success_url = reverse_lazy('profile')
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'Update Profile'
        return context

class PasswordChange(PasswordChangeView):
    template_name = 'register.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        return super().form_valid(form)