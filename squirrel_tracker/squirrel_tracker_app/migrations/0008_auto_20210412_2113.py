# Generated by Django 3.1.7 on 2021-04-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker_app', '0007_auto_20210412_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='hectare_squirrel_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Hectare Squirrel Number'),
        ),
    ]