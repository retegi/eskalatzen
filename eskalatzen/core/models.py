from django.db import models


# Create your models here.
class ClimbingSpot(models.Model):
    title = models.CharField(max_length=200, verbose_name='Sektorea')
    country = models.CharField(max_length=200, verbose_name='Herrialdea')
    ccaa = models.CharField(max_length=200, verbose_name='Autonomi erkidegoa')
    province = models.CharField(max_length=200, verbose_name='Probintzia')
    town = models.CharField(max_length=200, verbose_name='Herria')
    latitude = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='Latitudea')
    longitude = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='Latitudea')
    description = models.TextField(verbose_name='Deskribapena')
    image1 = models.ImageField(verbose_name='Irudia 1', upload_to="projects")
    image2 = models.ImageField(verbose_name='Irudia 2', upload_to="projects")
    image3 = models.ImageField(verbose_name='Irudia 3', upload_to="projects")
    link = models.URLField(verbose_name='Web helbidea', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Sektorea"
        verbose_name_plural = "Sektoreak"
        ordering = ["-created"]

    def __str__(self):
        return self.title
