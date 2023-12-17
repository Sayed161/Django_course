from django.urls import path
from . import views

urlpatterns = [
    path('musician/',views.musician, name='musician'),
    path('register/',views.register, name='register'),
    path('Login/',views.Login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('Logout/',views.user_logout, name='logout'),

]