from django.shortcuts import render
from rides.models import Ride


def index(request):
    return render(request, 'index.html')

def the_ride(request):
    # Get the ride - harcoded for the first run of this site.
    ride = Ride.objects.get(id = 2)
    return render(request, 'the_ride.html', {'ride': ride})

def the_charity(request):
    return render(request, 'the_charity.html')

def about(request):
    return render(request, 'about.html')

def sponsors(request):
	return render(request, 'sponsors.html')

def events(request):
    return render(request, 'events.html')
