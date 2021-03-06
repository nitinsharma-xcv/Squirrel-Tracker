from django.db import models


class Squirrel(models.Model):
    """
    Model class for storing sighted squirrel information
    """
    AM, PM = 'AM', 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'))

    x = models.FloatField('X', help_text='Geo Latitude')
    y = models.FloatField('Y', help_text='Geo Longitude')
    unique_squirrel_id = models.CharField('Unique Squirrel ID', max_length=255, primary_key=True,
                                          help_text='Squirrel Identifier')
    hectare = models.CharField('Hectare', max_length=255, help_text='Park Hectare Identifier')
    shift = models.CharField('Shift', max_length=2, choices=SHIFT_CHOICES)
    date = models.DateField('Date')
    hectare_squirrel_number = models.IntegerField('Hectare Squirrel Number', null=True, blank=True)
    age = models.CharField('Age', max_length=255, blank=True)
    primary_fur_color = models.CharField('Primary Fur Color', max_length=255, blank=True)
    highlight_fur_color = models.CharField('Highlight Fur Color', max_length=255, blank=True)
    combination_of_primary_and_highlight_color = models.CharField('Combination of Primary and Highlight Color',
                                                                  max_length=255, blank=True)
    color_notes = models.CharField('Color notes', max_length=255, blank=True)
    location = models.CharField('Location', max_length=255, blank=True)
    above_ground_sighter_measurement = models.CharField('Above Ground Sighter Measurement', max_length=255, blank=True)
    specific_location = models.CharField('Specific Location', max_length=255, blank=True)
    running = models.BooleanField('Running')
    chasing = models.BooleanField('Chasing')
    climbing = models.BooleanField('Climbing')
    eating = models.BooleanField('Eating')
    foraging = models.BooleanField('Foraging')
    other_activities = models.CharField('Other Activities', max_length=255, blank=True)
    kuks = models.BooleanField('Kuks')
    quaas = models.BooleanField('Quaas')
    moans = models.BooleanField('Moans')
    tail_flags = models.BooleanField('Tail flags')
    tail_twitches = models.BooleanField('Tail twitches')
    approaches = models.BooleanField('Approaches')
    indifferent = models.BooleanField('Indifferent')
    runs_from = models.BooleanField('Runs from')
    other_interactions = models.CharField('Other Interactions', max_length=255, blank=True)
    lat_long = models.CharField('Lat/Long', max_length=255, blank=True)

    def __str__(self):
        return f'<ID: {self.unique_squirrel_id}> {self.lat_long}'
