# Generated by Django 5.0.1 on 2024-01-16 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_coordinate_area_alter_crop_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='best_soil_type',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='best_temperature',
        ),
    ]
