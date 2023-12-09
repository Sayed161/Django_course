from django.shortcuts import render
from Album.models import albumsform
def home(request):
    data = albumsform.objects.all()
    return render(request, 'home.html',{'data':data})