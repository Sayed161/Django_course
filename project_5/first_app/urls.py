from django.urls import path
from first_app import views

urlpatterns = [
    path('about/', views.about, name= 'about'),
    path('form/', views.form,name='form'),
    path('Djangoform/', views.password,name='Django_form'),
]
