from django.shortcuts import render


def places_home(request):
    return render(request, 'places/places_home.html')