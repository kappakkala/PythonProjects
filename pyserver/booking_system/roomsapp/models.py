from django.db import models
from django.utils import timezone

# Create your models here.
class Available(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
    availability = models.DateField(default=timezone.now,blank=True)

class Booked(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
    availability = models.DateField(default=timezone.now,blank=True)
