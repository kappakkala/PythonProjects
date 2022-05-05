from django.db import models
from django.utils import timezone

# Create your models here.
class Rooms(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
    availability = models.DateField(default=timezone.now,blank=True)

class Available(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
    availability = models.DateField(default=timezone.now,blank=True)

class Booked(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
    availability = models.DateField(default=timezone.now,blank=True)

class Post(models.Model):
    buildings = models.CharField(max_length=10)
    def __str__(self):
        return f"self.building"