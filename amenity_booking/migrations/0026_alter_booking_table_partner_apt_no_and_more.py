# Generated by Django 4.1.4 on 2023-01-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0025_alter_booking_table_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_table',
            name='partner_apt_no',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='booking_table',
            name='partner_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
