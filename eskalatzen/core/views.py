from django.shortcuts import render
from .models import ClimbingSpot


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def maps(request):
    climbingspot = ClimbingSpot.objects.all()
    return render(request, "core/map.html", {'climbingspot': climbingspot})


def blog(request):
    return render(request, "core/blog.html")


def about(request):
    return render(request, "core/about.html")


def aritxulegi(request):
    climbingspot = ClimbingSpot.objects.get(title="Aritxulegi")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def pikoketa(request):
    climbingspot = ClimbingSpot.objects.get(title="Pikoketa")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def putakio(request):
    climbingspot = ClimbingSpot.objects.get(title="Putakio")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def weather(request):
    return render(request, "core/weather.html")
