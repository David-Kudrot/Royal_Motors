from django.urls import path
from .views import CarView

urlpatterns = [
    path('add/', CarView.as_view(), name='add'),
]
