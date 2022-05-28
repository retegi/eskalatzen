from django.shortcuts import render
from .models import ClimbingSpot, Camping, Video, MapBlog


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def maps(request):
    climbingspot = ClimbingSpot.objects.all()
    camping = Camping.objects.all()
    return render(request, "core/map.html", {'climbingspot': climbingspot, 'camping': camping})


def lista(request):
    climbingspot = ClimbingSpot.objects.all()
    return render(request, "core/lista.html", {'climbingspot': climbingspot, 'weather': weather})


def news(request):
    climbingspot = ClimbingSpot.objects.all()
    return render(request, "core/news.html")


def blog(request):
    mapblog = MapBlog.objects.all()
    return render(request, "core/blog.html", {'mapblog': mapblog})


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


def santabarbara(request):
    climbingspot = ClimbingSpot.objects.get(title="Santa Barbara")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def jentilbaratza(request):
    climbingspot = ClimbingSpot.objects.get(title="Jentilbaratza")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def txindoki(request):
    climbingspot = ClimbingSpot.objects.get(title="Txindoki")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def jaizkibel(request):
    climbingspot = ClimbingSpot.objects.get(title="Jaizkibel")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def amasola(request):
    climbingspot = ClimbingSpot.objects.get(title="Amasola")
    return render(request, "core/detail_view.html", {'climbingspot': climbingspot})


def weather(request):
    return render(request, "core/weather.html")


def video(request):
    videos = Video.objects.all()
    return render(request, "core/video.html", {'videos': videos})
