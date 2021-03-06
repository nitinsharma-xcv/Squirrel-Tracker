# import_squirrel_data.py
# Created on Mar 05, 2021 
# Author(s): Nitin Sharma (ns3493) <nitin.sharma@columbia.edu>

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
            pass  # TODO: Write import functionality
        except Exception as e:
            raise CommandError('Error', e)

        # self.stdout.write(self.style.SUCCESS(f'Successfully Imported {file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Functionality to be implemented'))
