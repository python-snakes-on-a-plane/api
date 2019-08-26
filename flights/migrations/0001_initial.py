# Generated by Django 2.2.4 on 2019-08-19 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('airborne', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatnumber', models.CharField(max_length=3)),
                ('flight', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
                ('passenger', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='flights.Passenger')),
            ],
        ),
    ]