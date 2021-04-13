from django.shortcuts import render, redirect
from .models import Squirrel
from .form import SquirrelFormUpdate, SquirrelFormAdd
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Min, Max, Count


def index(request):
    return render(request, 'squirrel_tracker_app/index.html', {})


def map_view(request):
    DEFAULT_LIMIT = 100
    coordinates = Squirrel.objects.values('x', 'y')[:DEFAULT_LIMIT]
    context = {'coordinates': coordinates}
    return render(request, 'squirrel_tracker_app/map.html', context)


def sightings(request):
    list_squirrels = Squirrel.objects.all()
    context = {'squirrels': list_squirrels}
    return render(request, 'squirrel_tracker_app/sightings.html', context)


def create(request):
    if request.method == 'Post':
        form = SquirrelFormAdd(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/sightings/')
    else:
        form = SquirrelFormAdd()
        return render(request, 'squirrel_tracker_app/add.html', {'form': form})


def add(request):
    form = SquirrelFormAdd(request.POST or None, )
    if form.is_valid():
        Object = form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        return render(request, 'squirrel_tracker_app/add.html', {'form': form})


def stats(request):
    squirrels = Squirrel.objects.all()
    total_squirrels = squirrels.count()
    latitude = squirrels.aggregate(minimum=Min('x'), maximum=Max('x'), avg=Avg('x'))
    date = squirrels.aggregate(minimum=Min('date'), maximum=Max('date'))
    longitude = squirrels.aggregate(minimum=Min('y'), maximum=Max('y'), avg=Avg('y'))
    age = list(squirrels.values_list('age').annotate(Count('age')))
    primary_fur_color = list(squirrels.values_list('primary_fur_color').annotate(Count('primary_fur_color')))
    running = list(squirrels.values_list('running').annotate(Count('running')))
    shift = list(squirrels.values_list('shift').annotate(Count('shift')))
    context = {'total_squirrels': total_squirrels,
               'latitude': latitude,
               'longitude': longitude,
               'date': date,
               'age': age,
               'primary_fur_color': primary_fur_color,
               'running': running,
               'shift': shift,
               }
    return render(request, 'squirrel_tracker_app/stats.html', context)


def update(request, unique_squirrel_id):
    obj = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    form = SquirrelFormUpdate(request.POST or None, instance=obj)
    if form.is_valid():
        Object = form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        return render(request, 'squirrel_tracker_app/update.html', {'form': form})
