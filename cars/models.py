from django.db import models
from brands.models import BrandModel

# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='images/', blank=True)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True, max_length=200)
    quantity = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.brand.name} - {self.name}"