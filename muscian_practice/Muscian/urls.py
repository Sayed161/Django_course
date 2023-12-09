from django.urls import path
from . import views

urlpatterns = [
    path('muscian/', views.muscian_view, name = 'muscian'),
]