"""eskalatzen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views as core_view

urlpatterns = [
    path('', core_view.maps, name="home"),
    path('Gipuzkoa/Aritxulegi/', core_view.aritxulegi, name="aritxulegi"),
    path('Gipuzkoa/Pikoketa/', core_view.pikoketa, name="pikoketa"),
    path('Gipuzkoa/Putakio/', core_view.putakio, name="putakio"),
    path('Gipuzkoa/Santa/', core_view.santabarbara, name="SantaBarbara"),
    path('Gipuzkoa/Txindoki/', core_view.txindoki, name="Txindoki"),
    path('Gipuzkoa/Jaizkibel/', core_view.jaizkibel, name="Jaizkibel"),
    path('Gipuzkoa/Jentilbaratza/', core_view.jentilbaratza, name="Jentilbaratza"),
    path('Gipuzkoa/Amasola/', core_view.amasola, name="Jentilbaratza"),
    path('lista/', core_view.lista, name="lista"),
    path('news/', core_view.news, name="news"),
    path('mapBlog/', core_view.blog, name="blog"),
    path('about/', core_view.about, name="about"),
    path('weather/', core_view.weather, name="eguraldia"),
    path('video/', core_view.video, name="video"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
