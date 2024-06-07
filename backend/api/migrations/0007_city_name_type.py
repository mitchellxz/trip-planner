# Generated by Django 5.0.6 on 2024-06-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_country_monthly_weather_avg'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_type',
            field=models.CharField(choices=[('City', 'City'), ('Village', 'Village'), ('Island', 'Island')], default='City', max_length=10),
        ),
    ]