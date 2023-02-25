# Generated by Django 4.1.5 on 2023-02-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0031_alter_booking_table_partner_apt_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='uidtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='amenity_type',
            options={'verbose_name_plural': 'Amenity Name Table'},
        ),
        migrations.AlterModelOptions(
            name='booking_table',
            options={'verbose_name_plural': 'Bookings Table'},
        ),
        migrations.AlterField(
            model_name='amenity_timings',
            name='timing',
            field=models.CharField(blank=True, choices=[('12AM-1AM', '12AM-1AM'), ('1AM-2AM', '1AM-2AM'), ('2AM-3AM', '2AM-3AM'), ('3AM-4AM', '3AM-4AM'), ('4AM-5AM', '4AM-5AM'), ('5AM-6AM', '5AM-6AM'), ('6AM-7AM', '6AM-7AM'), ('7AM-8AM', '7AM-8AM'), ('8AM-9AM', '8AM-9AM'), ('9AM-10AM', '9AM-10AM'), ('10AM-11AM', '10AM-11AM'), ('11AM-12PM', '11AM-12PM'), ('12PM-1PM', '12PM-1PM'), ('1PM-2PM', '1PM-2PM'), ('2PM-3PM', '2PM-3PM'), ('3PM-4PM', '3PM-4PM'), ('4PM-5PM', '4PM-5PM'), ('5PM-6PM', '5PM-6PM'), ('6PM-7PM', '6PM-7PM'), ('7PM-8PM', '7PM-8PM'), ('8PM-9PM', '8PM-9PM'), ('9PM-10PM', '9PM-10PM'), ('10PM-11PM', '10PM-11PM'), ('11PM-12AM', '11PM-12AM')], max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='amenity_slots',
            unique_together={('amenity_name', 'slot')},
        ),
        migrations.AlterUniqueTogether(
            name='amenity_timings',
            unique_together={('amenity_name', 'timing')},
        ),
    ]