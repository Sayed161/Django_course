from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUp,name = 'SignUp'),
    path('login/',views.Login,name = 'Login'),
    path('',views.home,name = 'home'),
    path('profile/',views.profile,name = 'Profile'),
    path('passchange/',views.change_pass,name = 'passchange'),
    path('passchange2/',views.change_pass2,name = 'passchange2'),
    path('logout/',views.user_logout,name = 'logout'),
]