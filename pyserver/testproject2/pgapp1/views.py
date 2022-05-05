from django.shortcuts import render
from .models import Rooms, Post, Available, Booked
import numpy as np
from .forms import Postbuilding, ContactUsForm, BuildingForm

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

def base2_view(request, *args, **kwargs):
    # building = request.POST.get('dropdown')
    # my_context = {"buildings" : building}
    # return render(request, "base2.html", my_context)
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = BuildingForm(request.POST)
        if len(request.POST['building']) != 0:
            name = 'Building '+ request.POST['building'] + ' is selected'
            queryset = Rooms.objects.filter(rooms__contains=request.POST['building'])
            rooms = [entry.rooms for entry in queryset]
        else:
            name = 'No building is selected'
            rooms = []
        if len(rooms) != 0:
            room_info = f"Available rooms are {rooms}"
        else:
            room_info = " "
    else:
        # this must be a GET request, so create an empty form
        form = BuildingForm()
        name = ''
        rooms = []
        room_info = ''
    book_date = request.GET.get('book_date')
    # if type(book_date) == type(None):
    #    book_date = ''
    queryset = Rooms.objects.filter(availability=book_date)
    available_rooms = [entry.rooms for entry in queryset]
    return render(request, "base2.html", {'form': form, 'building_info': name, 'room_info': room_info, 'available_rooms': available_rooms})


def search_view(request, *args, **kwargs):
    form = BuildingForm()
    building = request.GET.get('book_building')
    book_date = request.GET.get('book_date')
    queryset = Available.objects.filter(buildings=building, availability=book_date)
    available_rooms = [entry.rooms for entry in queryset]
    if len(available_rooms) != 0:
        info = f"Rooms available on {book_date} in building {building} are {available_rooms}."
    else:
        if (type(book_date) != type(None)) and (type(building) != type(None)):
            info = f"No rooms are available on {book_date} in building {building}."
        else:
            info = ''
    return render(request, "search.html", {'form': form, 'available_rooms': available_rooms, 'info_text': info})

def booking_view(request, *args, **kwargs):
    form = BuildingForm()
    room = request.GET.get('book_room')
    book_date = request.GET.get('book_date')
    queryset = Available.objects.filter(rooms=room, availability=book_date)
    booked_rooms = [entry.rooms for entry in queryset]
    building = [entry.buildings for entry in queryset]
    if len(booked_rooms) != 0:
        data = Booked(rooms=room, availability=book_date, buildings=building[0])
        data.save()
        queryset = Available.objects.filter(rooms=room, availability=book_date).delete()
        # [1, {'pgapp1.Rooms': 1}]
        info = f"Room {booked_rooms[0]} is booked on {book_date}."
    else:
        if (type(book_date) != type(None)) and (type(room) != type(None)):
            info = f"No rooms are booked on {book_date}. Check room selection."
        else:
            info = ''
    return render(request, "booking.html", {'form': form, 'booked_rooms': booked_rooms, 'info_text': info})

def cancel_view(request, *args, **kwargs):
    form = BuildingForm()
    room = request.GET.get('book_room')
    book_date = request.GET.get('book_date')
    queryset = Booked.objects.filter(rooms=room, availability=book_date)
    canceled_rooms = [entry.rooms for entry in queryset]
    building = [entry.buildings for entry in queryset]
    if len(canceled_rooms) != 0:
        data = Available(rooms=room, availability=book_date, buildings=building[0])
        data.save()
        queryset = Booked.objects.filter(rooms=room, availability=book_date).delete()
        # [1, {'pgapp1.Rooms': 1}]
        info = f"Room {canceled_rooms[0]} is canceled on {book_date}."
    else:
        if (type(book_date) != type(None)) and (type(room) != type(None)):
            info = f"No rooms are cancelled on {book_date}. Check room selection."
        else:
            info = ''
    return render(request, "cancel.html", {'form': form, 'canceled_rooms': canceled_rooms, 'info_text': info})