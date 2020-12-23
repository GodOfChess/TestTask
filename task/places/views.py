from django.shortcuts import render, redirect
from .models import Places
from .forms import PlacesForm
from django.contrib.auth import logout as auth_logout
from geopy.geocoders import Nominatim
import folium


def places_home(request):
    places = Places.objects.order_by('title')
    return render(request, 'places/places_home.html', {'places': places})


def create(request):
    error = ''
    geolocator = Nominatim(user_agent="places")
    m = folium.Map(width=400, height=250)

    if request.method == "POST":
        form = PlacesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            title_ = form.cleaned_data.get('title')
            title = geolocator.geocode(title_)
            instance.t_lat = title.latitude
            instance.t_lon = title.longitude
            instance.save()
            return redirect('/places')
        else:
            error = 'Форма заполнена неверно'


    form = PlacesForm()

    data = {
        'form': form,
        'error': error,
        'map': m,
    }

    return render(request, 'places/places_create.html', data)


def logout(request):
    auth_logout(request)
    return redirect('/')

