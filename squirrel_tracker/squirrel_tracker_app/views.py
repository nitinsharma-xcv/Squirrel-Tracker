from django.shortcuts import render, redirect
from .models import Squirrel
from .form import SquirrelFormUpdate, SquirrelFormAdd
from django.shortcuts import get_object_or_404
from random import sample
import pandas as pd


def index(request):
    return render(request, 'squirrel_tracker_app/index.html', {})


def details(request, unique_squirrel_id):
    squirrel = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    context = {'squirrel': squirrel}
    return render(request, 'squirrel_tracker_app/details.html', context)


def map_view(request):
    DEFAULT_LIMIT = 100
    coordinates = sample(list(Squirrel.objects.values('x', 'y')), DEFAULT_LIMIT)
    context = {'coordinates': coordinates}
    return render(request, 'squirrel_tracker_app/map.html', context)


def sightings(request):
    list_squirrels = Squirrel.objects.all().order_by('-date', 'unique_squirrel_id')
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


def update(request, unique_squirrel_id):
    obj = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    form = SquirrelFormUpdate(request.POST or None, instance=obj)
    if form.is_valid():
        Object = form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        return render(request, 'squirrel_tracker_app/update.html', {'form': form})


def stats(request):
    values = Squirrel.objects.all().values()
    df = pd.DataFrame(list(values))
    df.columns = [c.verbose_name for c in Squirrel._meta.get_fields()]

    def random_color():
        return 'rgb' + str(tuple(sample(range(256), 3)))

    context = {}

    # stat1
    fields1 = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging',
               'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from']
    stat1 = df.groupby('Shift')[fields1].sum().T
    stat1 = {
        'labels': stat1.index.tolist(),
        'AM_values': stat1['AM'].tolist(),
        'PM_values': stat1['PM'].tolist()
    }
    context['stat1'] = stat1

    # stat2
    primary = df['Primary Fur Color'].fillna('No Information').replace('', 'No Information').value_counts()
    stat2 = {
        'colors': primary.index.tolist(),
        'count': primary.tolist(),
        'colors_rgb': [random_color() for _ in range(len(primary))]
    }
    context['stat2'] = stat2

    # stat3
    highlight = df['Highlight Fur Color'].fillna('No Information').replace('', 'No Information').value_counts()
    stat3 = {
        'colors': highlight.index.tolist(),
        'count': highlight.tolist(),
        'colors_rgb': [random_color() for _ in range(len(highlight))],
    }
    context['stat3'] = stat3

    # stat4
    fields4 = ['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging',
               'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from']
    stat4 = df.groupby('Age')[fields4].sum().T
    adult_total, juvenile_total = (df['Age'] == 'Adult').sum(), (df['Age'] == 'Juvenile').sum()
    stat4 = {
        'labels': stat4.index.tolist(),
        'adult_values': (stat4['Adult'] * 100 / adult_total).tolist(),
        'juvenile_values': (stat4['Juvenile'] * 100 / juvenile_total).tolist()
    }
    context['stat4'] = stat4

    # stat5
    stat5 = df['Hectare'].dropna().value_counts()
    total_hectare = len(stat5)
    stat5 = stat5.sort_values(ascending=False)[:30]
    stat5 = {
        'total_hectare': total_hectare,
        'hectare': stat5.index.tolist(),
        'count': stat5.tolist()
    }
    context['stat5'] = stat5

    return render(request, 'squirrel_tracker_app/stats.html', context)
