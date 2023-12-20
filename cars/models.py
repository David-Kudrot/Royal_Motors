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
    
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name}"