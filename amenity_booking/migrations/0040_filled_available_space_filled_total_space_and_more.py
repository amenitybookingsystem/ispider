# Generated by Django 4.1.5 on 2023-02-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0039_filled'),
    ]

    operations = [
        migrations.AddField(
            model_name='filled',
            name='available_space',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='filled',
            name='total_space',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='filled',
            name='amenity_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filled',
            name='amenity_slot',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filled',
            name='amenity_timing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
