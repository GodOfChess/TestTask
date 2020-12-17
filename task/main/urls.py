from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='startpage'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('places/home', views.places_home, name='places_home')
]
