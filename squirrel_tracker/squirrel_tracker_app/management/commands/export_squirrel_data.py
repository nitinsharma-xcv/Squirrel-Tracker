# export_squirrel_data.py
# Created on Mar 05, 2021
# Author(s): Niharika Prasad (np2781) <niharika.prasad@columbia.edu>

from django.core.management.base import BaseCommand, CommandError
import csv
from ...models import Squirrel
import pandas as pd

class Command(BaseCommand):
    help = 'Command to export squirrel data to csv'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):

        try:
            file_path = options['file_path']
            #####
            vals = Squirrel.objects.all().values()
            df = pd.DataFrame(list(vals))
            df.columns = [c.replace('_', ' ').title() for c in df.columns]
            for bool_col in df.dtypes[df.dtypes == bool].index:
                df[bool_col] = df[bool_col].astype(str).str.upper()
            df['Date'] = df['Date'].apply(lambda d: d.strftime('%m%d%Y'))
            df.to_csv(file_path, index=False)

            breakpoint()
        #####


            with open(file_path, 'w') as f:
                open_to_write = csv.writer(f)
                fields = [field.name for field in Squirrel._meta.fields]
                field_type = [(type(field), field.name, field) for field in Squirrel._meta.fields]

                custom_field_name = [fi.replace('_', ' ').title() for fi in fields]
                open_to_write.writerow(custom_field_name)

                for i in Squirrel.objects.all():
                    row = []
                    for field in field_type:
                        if field[2].get_internal_type() == 'BooleanField':
                            row.append(str(getattr(i, field[1])).upper())
                        else:
                            row.append(str(getattr(i, field[1])))
                    # row = [str(getattr(i, field[1])) if field[2].get_internal_type() != 'BooleanField' else str(getattr(i, field[1])).upper() for field in type_ ]
                    open_to_write.writerow(row)
                f.close()
        except Exception as e:
            raise CommandError('Error', e)

        # self.stdout.write(self.style.SUCCESS(f'Successfully Imported {file_path}'))
        self.stdout.write(self.style.SUCCESS(f'Functionality to be implemented'))
