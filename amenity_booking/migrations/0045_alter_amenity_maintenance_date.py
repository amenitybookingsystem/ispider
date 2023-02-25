# Generated by Django 4.1.5 on 2023-02-24 13:14

import amenity_booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0044_alter_amenity_maintenance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity_maintenance',
            name='date',
            field=models.DateField(validators=[amenity_booking.models.validate_date]),
        ),
    ]