from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

from .models import ClimbingSpot, Camping, Video, MapBlog, \
    Euskalmet, OpenWeatherMap
from django.views.generic.detail import DetailView


# Create your views here.
def lang(request):
    trans = translate(language='fr')
    return render(request, 'core/lang.html', {'trans': trans})


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text


def home(request):
    return render(request, "core/home.html")


def maps(request):
    climbingspot = ClimbingSpot.objects.all()
    euskalmet = Euskalmet.objects.all()
    camping = Camping.objects.all()
    owms = OpenWeatherMap.objects.all()
    return render(request, "core/map.html", {'climbingspot': climbingspot,
                                             'camping': camping,
                                             'euskalmet': euskalmet,
                                             'owms': owms})


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


def ikastaroak(request):
    return render(request, "core/courses.html")


def data(request):
    return render(request, "core/data.html")


class PostDetailView(DetailView):
    model = ClimbingSpot
    template_name = 'detail_view.html'

    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['climbingspots'] = ClimbingSpot.objects.all()
        print(f"name {name}")
        context['climbingspot'] = ClimbingSpot.objects.filter(title=name)
        return context
