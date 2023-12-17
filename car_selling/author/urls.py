from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    
    path('login/', views.LoginForm.as_view(),name='login'),
    path('logout/', views.LogOutForm.as_view(),name='logout'),

    path('profile/', views.profile_login,name='profile'),
    path('profile/<int:id>', views.profile_login,name='profile'),
    path('edit/', views.edit_profile,name='edit'),
    
]