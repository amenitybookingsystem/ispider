# Generated by Django 4.1.4 on 2023-01-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0016_amenity_amenity_timings_amenity_slots'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='amenity',
            new_name='amenity_name',
        ),
        migrations.RenameField(
            model_name='amenity_slots',
            old_name='amenity',
            new_name='amenity_name',
        ),
        migrations.RenameField(
            model_name='amenity_timings',
            old_name='amenity',
            new_name='amenity_name',
        ),
        migrations.AlterField(
            model_name='amenity_timings',
            name='timing',
            field=models.CharField(blank=True, choices=[('time1', '6AM-7AM'), ('time2', '7AM-8AM'), ('time3', '8AM-9AM'), ('time4', '9AM-10AM')], max_length=100, null=True),
        ),
    ]
