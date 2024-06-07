# Generated by Django 5.0.6 on 2024-06-05 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_country_monthly_weather_avg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='popular_cities',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='api.country')),
            ],
            options={
                'unique_together': {('name', 'country')},
            },
        ),
    ]