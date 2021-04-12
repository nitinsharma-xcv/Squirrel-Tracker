from django.http import HttpResponse
from django.shortcuts import render
from .models import Squirrel


def index(request):
    return HttpResponse("Hello, world!")


def list_of_squirrels(request):
    list_squirrels = Squirrel.objects.all()
    context = {'squirrels': list_squirrels}
    return render(request, 'squirrel_tracker_app/list_all_squirrels.html', context)
