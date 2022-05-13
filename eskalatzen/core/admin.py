from django.contrib import admin
from .models import ClimbingSpot


# Register your models here.
class ClimbingSpotAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(ClimbingSpot, ClimbingSpotAdmin)
