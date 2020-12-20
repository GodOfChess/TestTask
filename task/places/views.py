from django.shortcuts import render, redirect
from .models import Places
from .forms import PlacesForm

def places_home(request):
    places = Places.objects.order_by('title')
    return render(request, 'places/places_home.html', {'places': places})

def create(request):
    error=''
    if request.method == "POST":
        form = PlacesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places_home')
        else:
            error='Форма заполнена неверно'

    form = PlacesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'places/places_create.html',data)
