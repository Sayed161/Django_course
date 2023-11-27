from django.urls import path
from navigation import views

urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact),
    # path("navigation/", include("navigation.urls")),
]