# Generated by Django 4.1.5 on 2023-02-25 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0052_alter_amenity_slots_amenity_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='amenity_maintenance',
            unique_together={('slot', 'time', 'date')},
        ),
    ]
