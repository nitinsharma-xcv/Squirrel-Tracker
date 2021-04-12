from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel


def index(request):
    return render(request, 'squirrel_tracker_app/index.html', {})


def map_view(request):
    DEFAULT_LIMIT = 100
    coordinates = Squirrel.objects.values('x', 'y')[:DEFAULT_LIMIT]
    context = {'coordinates': coordinates}
    return render(request, 'squirrel_tracker_app/map.html', context)
