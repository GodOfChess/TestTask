from django.urls import path
from . import views

urlpatterns = [
    path('',views.places_home,name='places_home')
]
