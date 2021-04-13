from django import forms
from .models import Squirrel


class SquirrelFormUpdate(forms.ModelForm):
    class Meta:
        model = Squirrel
        fields = ['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age']


class SquirrelFormAdd(forms.ModelForm):
    class Meta:
        model = Squirrel
        fields = ['x', 'y', 'unique_squirrel_id', 'shift', 'date', 'hectare_squirrel_number','age',
                  'primary_fur_color', 'location', 'specific_location', 'running', 'chasing',
                  'climbing', 'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans',
                  'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from']
