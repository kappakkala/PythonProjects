from django.db import models

# Create your models here.
class Rooms(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)

class Post(models.Model):
    buildings = models.CharField(max_length=10)
    def __str__(self):
        return f"self.building"