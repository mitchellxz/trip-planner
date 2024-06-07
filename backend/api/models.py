from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    
class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    monthly_weather_avg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    CITY = "City"
    VILLAGE = "Village"
    ISLAND = "Island"
    TOWN = "Town"

    NAME_TYPE_CHOICES = {
        CITY: "City",
        VILLAGE: "Village",
        ISLAND: "Island",
        TOWN: "Town",
    }

    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)
    name_type = models.CharField(
        max_length=10,
        choices=NAME_TYPE_CHOICES,
        default=CITY,
    )

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name