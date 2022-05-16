from django.db import models


# Create your models here.
class ClimbingSpot(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Sektorea')
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herrialdea')
    ccaa = models.CharField(max_length=200, null=True, blank=True, verbose_name='Autonomi erkidegoa')
    province = models.CharField(max_length=200, null=True, blank=True, verbose_name='Probintzia')
    town = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herria')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitudea')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitudea')
    stone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Harria')
    description = models.TextField(null=True, blank=True, verbose_name='Deskribapena')
    image1 = models.ImageField(null=True, blank=True, verbose_name='Irudia 1', upload_to="projects")
    image2 = models.ImageField(null=True, blank=True, verbose_name='Irudia 2', upload_to="projects")
    image3 = models.ImageField(null=True, blank=True, verbose_name='Irudia 3', upload_to="projects")
    image4 = models.ImageField(null=True, blank=True, verbose_name='Irudia 4', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Sektorea"
        verbose_name_plural = "Sektoreak"
        ordering = ["created"]

    def __str__(self):
        return self.title
