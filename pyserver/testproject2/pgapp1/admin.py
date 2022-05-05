from django.contrib import admin
from .models import Rooms, Available, Booked

# Register your models here.

admin.site.register(Rooms)
admin.site.register(Available)
admin.site.register(Booked)
