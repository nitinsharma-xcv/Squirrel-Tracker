# import_squirrel_data.py
# Created on Mar 05, 2021 
# Author(s): Nitin Sharma (ns3493) <nitin.sharma@columbia.edu>,
#            Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from datetime import datetime
import csv
from django.core.management.base import BaseCommand, CommandError
from ...models import Squirrel


def to_bool(string):
    return True if string.upper() == 'TRUE' else False


class Command(BaseCommand):
    help = 'Imports data from given file into Squirrel-Tracker application'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
            with open(file_path) as file:
                data = csv.DictReader(file)
                self.import_data(data)
        except Exception as e:
            raise CommandError(e)

    def import_data(self, data):
        failed_records = []
        for i, record in enumerate(data):
            try:
                instance = Squirrel(
                    unique_squirrel_id=record['Unique Squirrel ID'],
                    x=record['X'],
                    y=record['Y'],
                    hectare=record['Hectare'],
                    shift=record['Shift'],
                    date=datetime.strptime(str(record['Date']), '%m%d%Y').date(),
                    hectare_squirrel_number=record['Hectare Squirrel Number'],
                    age=record['Age'],
                    primary_fur_color=record['Primary Fur Color'],
                    highlight_fur_color=record['Highlight Fur Color'],
                    combination_of_primary_and_highlight_color=record['Combination of Primary and Highlight Color'],
                    color_notes=record['Color notes'],
                    location=record['Location'],
                    above_ground_sighter_measurement=record['Above Ground Sighter Measurement'],
                    specific_location=record['Specific Location'],
                    running=to_bool(record['Running']),
                    chasing=to_bool(record['Chasing']),
                    climbing=to_bool(record['Climbing']),
                    eating=to_bool(record['Eating']),
                    foraging=to_bool(record['Foraging']),
                    other_activities=record['Other Activities'],
                    kuks=to_bool(record['Kuks']),
                    quaas=to_bool(record['Quaas']),
                    moans=to_bool(record['Moans']),
                    tail_flags=to_bool(record['Tail flags']),
                    tail_twitches=to_bool(record['Tail twitches']),
                    approaches=to_bool(record['Approaches']),
                    indifferent=to_bool(record['Indifferent']),
                    runs_from=to_bool(record['Runs from']),
                    other_interactions=record['Other Interactions'],
                    lat_long=record['Lat/Long']
                )
                instance.save()
            except Exception as e:
                failed_records.append({'row': i + 1, 'error': e})

        self.handle_failed_records(failed_records)

    def handle_failed_records(self, failed_records):
        if failed_records:
            for record in failed_records:
                self.stdout.write(self.style.ERROR(f"Import of Row {record['row']} failed. {record['error']}"))
        else:
            self.stdout.write(self.style.SUCCESS('Data Successfully Imported'))
