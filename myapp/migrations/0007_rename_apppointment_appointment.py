# Generated by Django 4.0.5 on 2022-07-07 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_apppointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apppointment',
            new_name='Appointment',
        ),
    ]