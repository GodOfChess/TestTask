from django.urls import path
from . import views


urlpatterns = [
    path('',views.places_home,name='places_home'),
    path('create', views.create,name='places_create'),
    path('logout', views.logout,name='exit'),
]
