# Generated by Django 4.1.4 on 2023-01-22 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0017_rename_amenity_amenity_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='amenity_name',
            new_name='amenity_type',
        ),
    ]
