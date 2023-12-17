from django.shortcuts import render
from brand_model.models import brand
from car_model.models import Cars
from django.views.generic import DetailView

def home(request,brand_slug=None):
    data = brand.objects.all()
    if brand_slug is not None:
        brands = brand.objects.get(slug=brand_slug)
        data = Cars.objects.filter(Brand=brands)
    car = Cars.objects.all()
    return render(request,'home.html',{'data':data,'car':car})


