# Generated by Django 4.1.1 on 2023-01-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0004_login_table_apt_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
