# Generated by Django 4.2.6 on 2024-01-16 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_crop_image_crop_image_blob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='image_blob',
            new_name='image',
        ),
    ]