from django.shortcuts import render
from .models import Rooms, Post
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


def base3_view(request, *args, **kwargs):
    my_context = {}
    return render(request, "base3.html", my_context)

def contact_view(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)
        name = request.POST['name']
    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()
    return render(request, "contact.html", {'form': form, 'name': name})  # pass that form to the template