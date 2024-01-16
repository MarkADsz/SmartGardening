# Generated by Django 5.0.1 on 2024-01-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_coordinate_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinate',
            name='area',
            field=models.FloatField(default=2.3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crop',
            name='type',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]