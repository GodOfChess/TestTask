from django.shortcuts import render


def index(request):
    return render(request, 'main/startpage.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

def places_home(request):
    return render(request, 'places/places_home.html')