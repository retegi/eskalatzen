from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'core'

urlpatterns = [
    path(
        'detail_view/<pk>/',
        views.PostDetailView.as_view(),
        name='detail_view'
    ),

    path('Gipuzkoa/Aritxulegi/', views.aritxulegi, name="aritxulegi"),
    path('Gipuzkoa/Pikoketa/', views.pikoketa, name="pikoketa"),
    path('Gipuzkoa/Putakio/', views.putakio, name="putakio"),
    path('Gipuzkoa/Santa/', views.santabarbara, name="SantaBarbara"),
    path('Gipuzkoa/Txindoki/', views.txindoki, name="Txindoki"),
    path('Gipuzkoa/Jaizkibel/', views.jaizkibel, name="Jaizkibel"),
    path('Gipuzkoa/Jentilbaratza/', views.jentilbaratza, name="Jentilbaratza"),
    path('Gipuzkoa/Amasola/', views.amasola, name="Jentilbaratza"),

]

