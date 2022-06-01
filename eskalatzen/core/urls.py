from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    path('', include('lang.urls', namespace='lang'))
]

urlpatterns += i18n_patterns (
    path('', include('lang.urls', namespace='lang'))
)

