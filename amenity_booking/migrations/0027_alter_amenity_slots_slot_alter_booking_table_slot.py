# Generated by Django 4.1.1 on 2023-01-25 07:00

import amenity_booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0026_alter_booking_table_partner_apt_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity_slots',
            name='slot',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[amenity_booking.models.validate_slots]),
        ),
        migrations.AlterField(
            model_name='booking_table',
            name='slot',
            field=models.CharField(max_length=30, verbose_name='Slot Name'),
        ),
    ]
