from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.Login,name='login'),
    path('logout/', views.LogOut,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('edit/', views.edit_pass,name='edit'),
]