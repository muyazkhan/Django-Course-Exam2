from django.shortcuts import render
from profiles import models


def home(request, brand=None):
    cars = models.Car.objects.all()
    if brand is not None:
        singleBrand = models.Brand.objects.get(slug=brand)
        cars = models.Car.objects.filter(brand=singleBrand)
    brands = models.Brand.objects.all()
    print(brand)
    return render(request, "home.html", {"brands": brands, "cars": cars})
  

