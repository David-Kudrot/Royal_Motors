from django.db import models
from django.contrib.auth.models import User
from cars.models import CarModel

# Create your models here.
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date=models.DateTimeField(auto_now_add=True)