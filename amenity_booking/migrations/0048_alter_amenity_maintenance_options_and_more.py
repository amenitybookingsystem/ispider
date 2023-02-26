# Generated by Django 4.1.5 on 2023-02-25 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0047_amenity_type_base_rate_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity_maintenance',
            options={'verbose_name_plural': '8) Amenity Maintenance Table'},
        ),
        migrations.AlterModelOptions(
            name='amenity_slots',
            options={'verbose_name_plural': '6) Amenity Slots Table'},
        ),
        migrations.AlterModelOptions(
            name='amenity_timings',
            options={'verbose_name_plural': '7) Amenity Timing Table'},
        ),
        migrations.AlterModelOptions(
            name='amenity_type',
            options={'verbose_name_plural': '5) Amenity Name Table'},
        ),
        migrations.AlterModelOptions(
            name='booking_table',
            options={'verbose_name_plural': '3) Bookings Table'},
        ),
        migrations.AlterModelOptions(
            name='contact_table',
            options={'verbose_name_plural': '4) Contact Table'},
        ),
        migrations.AlterModelOptions(
            name='filled',
            options={'verbose_name_plural': '10) System Info'},
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name_plural': '1) Master Table'},
        ),
        migrations.AlterModelOptions(
            name='signup_table',
            options={'verbose_name_plural': '2) Signup Table'},
        ),
        migrations.AlterModelOptions(
            name='uidtable',
            options={'verbose_name_plural': '9) System Info'},
        ),
    ]
