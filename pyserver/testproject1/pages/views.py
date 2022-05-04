from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Django Server!</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {"name" : "jason", "id" : 72}
    return render(request, "about.html", my_context)