# Generated by Django 4.1.5 on 2023-02-24 03:43

import amenity_booking.models
from django.db import migrations, models
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0033_amenity_type_allow_multiple_bookings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity_slots',
            name='slot',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[functools.partial(amenity_booking.models.validate_slots, *(), **{})]),
        ),
        migrations.AlterField(
            model_name='amenity_type',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[functools.partial(amenity_booking.models.validate_amenity, *(), **{})]),
        ),
    ]
