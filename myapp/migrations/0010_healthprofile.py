# Generated by Django 4.0.5 on 2022-07-14 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cencelappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('diabetes', models.BooleanField(default=False)),
                ('blood_pressure', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
