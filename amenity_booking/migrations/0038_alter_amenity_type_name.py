# Generated by Django 4.1.5 on 2023-02-24 04:18

import amenity_booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0037_alter_amenity_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity_type',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[amenity_booking.models.validate_amenity]),
        ),
    ]
