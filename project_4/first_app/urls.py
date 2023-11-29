from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path("about/", views.about, name  = 'about'),
]