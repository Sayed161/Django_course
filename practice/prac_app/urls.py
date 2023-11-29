from django.urls import path,include
from prac_app import views

urlpatterns = [
        path('about/', views.about),
        path('contact/', views.contact),
]