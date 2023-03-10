# Generated by Django 4.1.4 on 2023-01-22 07:25

import amenity_booking.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0015_remove_amenity_config_table_hours_active_from_6am_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, validators=[amenity_booking.models.validate_amenity])),
            ],
        ),
        migrations.CreateModel(
            name='amenity_timings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.CharField(blank=True, choices=[('6AM-7AM', 'time1'), ('7AM-8AM', 'time2'), ('8AM-9AM', 'time3'), ('9AM-10AM', 'time4')], max_length=100, null=True)),
                ('amenity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amenity_booking.amenity')),
            ],
        ),
        migrations.CreateModel(
            name='amenity_slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(blank=True, max_length=100, null=True)),
                ('amenity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amenity_booking.amenity')),
            ],
        ),
    ]
