from django.urls import path
from Author import views

urlpatterns = [
    path('register/',views.register,name = 'register'), 
    path('login/',views.user_login,name = 'user_login'), 
    path('logOut/',views.user_logout,name = 'user_logout'), 
    path('profile/',views.profile,name = 'profile'), 
    path('profile/edit/',views.edit_profile,name = 'edit_profile'), 
    path('profile/edit/passChange/',views.pass_change,name = 'pass_change'), 
]