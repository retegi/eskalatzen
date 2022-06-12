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
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('lang', core_view.lang, name="lang"),
    path('', core_view.maps, name="home"),
    path('', include('core.urls')),
    path('lista/', core_view.lista, name="lista"),
    path('news/', core_view.news, name="news"),
    path('ikastaroak/', core_view.ikastaroak, name="ikastaroak"),
    path('mapBlog/', core_view.blog, name="blog"),
    path('data/', core_view.data, name="data"),
    path('about/', core_view.about, name="about"),
    path('weather/', core_view.weather, name="eguraldia"),
    path('video/', core_view.video, name="video"),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
