# Generated by Django 5.0.6 on 2024-06-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='monthly_weather_avg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
