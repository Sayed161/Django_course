from django.urls import path
from . import views

urlpatterns = [
    path('album/',views.album, name='album'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('delete/<int:id>',views.post_delete, name='delete'),

]