# Generated by Django 2.2.4 on 2021-06-03 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdreams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='room',
            name='check_out',
        ),
        migrations.RemoveField(
            model_name='room',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='room',
            name='is_booked',
        ),
    ]
