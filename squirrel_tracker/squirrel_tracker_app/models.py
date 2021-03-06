from django.db import models


class Squirrel(models.Model):
    """
    Model class for storing sighted squirrel information
    """
    AM, PM = 'AM', 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'))

    unique_squirrel_id = models.CharField('Unique Squirrel ID', max_length=255, primary_key=True,
                                          help_text='Squirrel Identifier')
    x = models.FloatField('Latitude', help_text='Geo Latitude')
    y = models.FloatField('Longitude', help_text='Geo Longitude')
    hectare = models.CharField('Hectare', max_length=255, help_text='Park Hectare Identifier')
    shift = models.CharField('Shift', max_length=2, choices=SHIFT_CHOICES)
    date = models.DateField('Date')
    hectare_squirrel_number = models.IntegerField('Hectare Squirrel Number')
    age = models.CharField('Age', max_length=255)
    primary_fur_color = models.CharField('Primary Fur Color', max_length=255)
    highlight_fur_color = models.CharField('Highlight Fur Color', max_length=255)
    combination_of_primary_and_highlight_color = models.CharField('Combination of Primary and Highlight Color',
                                                                  max_length=255)
    color_notes = models.CharField('Color notes', max_length=255)
    location = models.CharField('Location', max_length=255)
    above_ground_sighter_measurement = models.CharField('Above Ground Sighter Measurement', max_length=255)
    specific_location = models.CharField('Specific Location', max_length=255)
    running = models.BooleanField('Running')
    chasing = models.BooleanField('Chasing')
    climbing = models.BooleanField('Climbing')
    eating = models.BooleanField('Eating')
    foraging = models.BooleanField('Foraging')
    other_activities = models.CharField('Other Activities', max_length=255)
    kuks = models.BooleanField('Kuks')
    quaas = models.BooleanField('Quaas')
    moans = models.BooleanField('Moans')
    tail_flags = models.BooleanField('Tail flags')
    tail_twitches = models.BooleanField('Tail twitches')
    approaches = models.BooleanField('Approaches')
    indifferent = models.BooleanField('Indifferent')
    runs_from = models.BooleanField('Runs from')
    other_interactions = models.CharField('Other Interactions', max_length=255)
