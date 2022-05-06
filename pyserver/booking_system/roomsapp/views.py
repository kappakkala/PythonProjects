from django.shortcuts import render
from .models import Available, Booked
import numpy as np

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "home.html", my_context)

def search_view(request, *args, **kwargs):
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
    return render(request, "search.html", {'available_rooms': available_rooms, 'info_text': info})

def booking_view(request, *args, **kwargs):
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
    return render(request, "booking.html", {'booked_rooms': booked_rooms, 'info_text': info})

def cancel_view(request, *args, **kwargs):
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
    return render(request, "cancel.html", {'canceled_rooms': canceled_rooms, 'info_text': info})