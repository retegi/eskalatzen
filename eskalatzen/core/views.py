from django.shortcuts import render
from .models import ClimbingSpot


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def maps(request):
    climbingspot = ClimbingSpot.objects.all()
    return render(request, "core/map.html", {'climbingspot': climbingspot})

# def maps(request):
#     return render(request, "core/map.html")


def blog(request):
    return render(request, "core/blog.html")


def about(request):
    return render(request, "core/about.html")



