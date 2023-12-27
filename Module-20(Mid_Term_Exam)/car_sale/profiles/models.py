from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/',blank=True,null=True)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.brand} - {self.model_name}"

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"