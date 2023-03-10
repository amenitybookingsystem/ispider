# Generated by Django 4.1.4 on 2023-01-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0007_booking_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='id',
        ),
        migrations.AlterField(
            model_name='master',
            name='apt_no',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='master',
            name='last_name',
            field=models.CharField(blank=True, default='none', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup_table',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='signup_table',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
