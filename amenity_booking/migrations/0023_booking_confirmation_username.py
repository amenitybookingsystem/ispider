# Generated by Django 4.1.4 on 2023-01-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0022_booking_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_confirmation',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
