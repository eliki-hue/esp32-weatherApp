# Generated by Django 5.0.3 on 2024-03-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
