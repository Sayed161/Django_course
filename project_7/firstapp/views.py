from django.shortcuts import render
from firstapp import forms
# Create your views here.
def home(request):
    std = forms.studentforms()
    return render(request, 'home.html', {'form': std})