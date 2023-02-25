# Generated by Django 4.1.4 on 2023-01-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0005_contact_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login_table',
        ),
        migrations.RemoveField(
            model_name='signup_table',
            name='password',
        ),
        migrations.AddField(
            model_name='master',
            name='email',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
