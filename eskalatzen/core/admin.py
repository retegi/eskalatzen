from django.contrib import admin
from .models import ClimbingSpot, Weather


# Register your models here.
class ClimbingSpotAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class WeatherAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(ClimbingSpot, ClimbingSpotAdmin)
admin.site.register(Weather, WeatherAdmin)
