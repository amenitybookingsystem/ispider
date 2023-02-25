# Generated by Django 4.1.4 on 2023-01-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0018_rename_amenity_name_amenity_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='amenity_config_table',
        ),
        migrations.AlterField(
            model_name='amenity_timings',
            name='timing',
            field=models.CharField(blank=True, choices=[('6AM-7AM', '6AM-7AM'), ('7AM-8AM', '7AM-8AM'), ('8AM-9AM', '8AM-9AM'), ('9AM-10AM', '9AM-10AM')], max_length=100, null=True),
        ),
    ]
