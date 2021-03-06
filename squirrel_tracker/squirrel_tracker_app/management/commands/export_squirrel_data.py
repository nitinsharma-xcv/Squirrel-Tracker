# export_squirrel_data.py
# Created on Mar 05, 2021
# Author(s): Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from django.core.management.base import BaseCommand, CommandError
import csv
from ...models import Squirrel


class Command(BaseCommand):
    help = 'Command to export squirrel data to csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
             pass  # TODO: Write export functionality

        except Exception as e:
            raise CommandError('Error', e)

        # self.stdout.write(self.style.SUCCESS(f'Successfully Imported {file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Functionality to be implemented'))
