# Generated by Django 4.1.4 on 2023-01-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenity_booking', '0002_signup_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]