from django.urls import path
from Author import views

urlpatterns = [
    path('add/',views.add_author,name = 'add_author'), 
]