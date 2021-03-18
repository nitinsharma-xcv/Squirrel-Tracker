# export_squirrel_data.py
# Created on Mar 05, 2021
# Author(s): Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from django.core.management.base import BaseCommand, CommandError
from ...models import Squirrel
import pandas as pd


class Command(BaseCommand):
    help = 'Command to export squirrel data to csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        try:
            file_path = options['file_path']
            values = Squirrel.objects.all().values()
            df = pd.DataFrame(list(values))
            df.columns = [c.verbose_name for c in Squirrel._meta.get_fields()]

            for bool_col in df.dtypes[df.dtypes == bool].index:
                df[bool_col] = df[bool_col].astype(str).str.lower()

            df['Date'] = df['Date'].apply(lambda d: d.strftime('%m%d%Y'))
            df['Lat/Long'] = [obj.lat_long for obj in Squirrel.objects.all()]

            df.to_csv(file_path, index=False)
        except Exception as e:
            raise CommandError('Error', e)

        self.stdout.write(self.style.SUCCESS(f'Data Successfully Exported to {file_path}'))
