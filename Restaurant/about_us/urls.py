from django.urls import path
from about_us import views

urlpatterns = [
    path('about/', views.about, name='about_us'),
]