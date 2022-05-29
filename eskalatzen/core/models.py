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
    difficulty = models.CharField(max_length=200, null=True, blank=True, verbose_name='Zailtasuna')
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


class MapBlog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Sektorea')
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herrialdea')
    ccaa = models.CharField(max_length=200, null=True, blank=True, verbose_name='Autonomi erkidegoa')
    province = models.CharField(max_length=200, null=True, blank=True, verbose_name='Probintzia')
    town = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herria')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitudea')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitudea')
    stone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Harria')
    difficulty = models.CharField(max_length=200, null=True, blank=True, verbose_name='Zailtasuna')
    description = models.TextField(null=True, blank=True, verbose_name='Deskribapena')
    image1 = models.ImageField(null=True, blank=True, verbose_name='Irudia 1', upload_to="projects")
    image2 = models.ImageField(null=True, blank=True, verbose_name='Irudia 2', upload_to="projects")
    image3 = models.ImageField(null=True, blank=True, verbose_name='Irudia 3', upload_to="projects")
    image4 = models.ImageField(null=True, blank=True, verbose_name='Irudia 4', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Bidaia"
        verbose_name_plural = "Bidaiak"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Camping(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    town = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herria')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Helbidea')
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name='Web orria')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Telefono zenbakia')
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name='Deskribapena')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitudea')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitudea')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Kanpina"
        verbose_name_plural = "Kanpinak"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    town = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herria')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Helbidea')
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name='Web orria')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Telefono zenbakia')
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name='Deskribapena')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitudea')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitudea')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Material alokairua"
        verbose_name_plural = "Material alokairua"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    link = models.CharField(max_length=200, null=True, blank=True, verbose_name='link')
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name='Deskribapena')
    section = models.CharField(max_length=200, null=True, blank=True, verbose_name='Atala')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Bideoa"
        verbose_name_plural = "Bideoak"
        ordering = ["created"]

    def __str__(self):
        return self.title


class Euskalmet(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    town = models.CharField(max_length=200, null=True, blank=True, verbose_name='Herria')
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name='Deskribapena')
    text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Text')
    tempMax = models.FloatField(null=True, blank=True, verbose_name='temp max')
    tempMin = models.FloatField(null=True, blank=True, verbose_name='temp min')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Latitudea')
    longitude = models.FloatField(null=True, blank=True, verbose_name='Longitudea')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Euskalmet"
        verbose_name_plural = "Euskalmet"
        ordering = ["created"]

    def __str__(self):
        return self.title


class OpenWeatherMap(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Izena')
    owm = models.CharField(max_length=200, null=True, blank=True, verbose_name='code')
    path = models.CharField(max_length=200, null=True, blank=True, verbose_name='webpath')
    icon = models.ImageField(null=True, blank=True, verbose_name='Icon', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "OpenWeatherMap"
        verbose_name_plural = "OpenWeatherMap"
        ordering = ["created"]

    def __str__(self):
        return self.title
