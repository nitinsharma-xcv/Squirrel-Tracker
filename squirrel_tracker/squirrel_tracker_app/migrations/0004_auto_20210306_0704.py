# Generated by Django 3.1.7 on 2021-03-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker_app', '0003_auto_20210306_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(blank=True, max_length=255, verbose_name='Other Activities'),
        ),
    ]