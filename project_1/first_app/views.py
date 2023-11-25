from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This is a list of courses")
def about(request):
    return HttpResponse("This is a about us")
def homepage(request):
    return HttpResponse("This is a first_app home page us")
