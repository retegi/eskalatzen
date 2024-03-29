from django.contrib import admin
from .models import ClimbingSpot, Camping, Location, Video
from .models import MapBlog, Euskalmet, OpenWeatherMap


# Register your models here.
class ClimbingSpotAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CampingAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class MapBlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class EuskalmetAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class OpenWeatherMapAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(ClimbingSpot, ClimbingSpotAdmin)
admin.site.register(Camping, CampingAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(MapBlog, MapBlogAdmin)
admin.site.register(Euskalmet, EuskalmetAdmin)
admin.site.register(OpenWeatherMap, OpenWeatherMapAdmin)
