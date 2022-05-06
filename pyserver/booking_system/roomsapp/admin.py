from django.contrib import admin
from .models import Available, Booked

# Register your models here.
admin.site.register(Available)
admin.site.register(Booked)