# Generated by Django 4.1.5 on 2023-02-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0043_alter_amenity_slots_amenity_name_amenity_maintenance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity_maintenance',
            name='date',
            field=models.DateField(),
        ),
    ]
