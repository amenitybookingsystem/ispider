# Generated by Django 4.1.5 on 2023-02-25 17:03

import amenity_booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0055_alter_master_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_table',
            name='apt_no',
            field=models.CharField(max_length=3, validators=[amenity_booking.models.validate_apt_no]),
        ),
    ]