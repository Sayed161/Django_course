from django.urls import path,include
from meal import views

urlpatterns = [
    path('meals/', views.meals, name='meal'),
]
