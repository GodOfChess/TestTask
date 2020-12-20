from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('',views.places_home,name='places_home'),
    path('create', views.create,name='places_create'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit')
]
