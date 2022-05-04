from django.shortcuts import render
from .models import Rooms, Post
import numpy as np
from .forms import Postbuilding

# Create your views here.
def home_view(request, *args, **kwargs):
    buildings = str(np.unique([entry[0] for entry in Rooms.objects.values_list('buildings')]))
    # queryset = Rooms.objects.filter(rooms__contains='A')
    # rooms = [entry.rooms for entry in queryset]
    rooms = str([entry[0] for entry in Rooms.objects.values_list('rooms')])
    my_context = {"buildings" : buildings, "rooms" : rooms}
    return render(request, "home.html", my_context)

def base1_view(request, *args, **kwargs):
    if request.method == "POST":
        buildings = Postbuilding(request.Post)
    else:
        buildings = Postbuilding()
    # buildings = str(np.unique([entry[0] for entry in Rooms.objects.values_list('buildings')]))
    # queryset = Rooms.objects.filter(rooms__contains='A')
    # rooms = [entry.rooms for entry in queryset]
    rooms = str([entry[0] for entry in Rooms.objects.values_list('rooms')])
    my_context = {"buildings" : buildings, "rooms" : rooms}
    return render(request, "base1.html", my_context)