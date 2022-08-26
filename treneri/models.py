from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import Resize, ResizeToFill, Thumbnail, ResizeToCover, SmartResize, ResizeToFit, ResizeCanvas

# Create your models here.

class Klub(models.Model):
    ime_kluba = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ime_kluba


class Trener(models.Model):
    REGION = (
        ('Vojvodina', 'Vojvodina'),
        ('Beograd', 'Beograd'),
        ('Istočna Srbija', 'Istočna Srbija'),
        ('Zapadna Srbija', 'Zapadna Srbija'),
        ('Juzna Srbija', 'Juzna Srbija'),
        ('Republika Srpska', 'Republika Srpska'),
        ('Inostranstvo', 'Inostranstvo'),
    )

    ime = models.CharField(max_length=100)
    licenca = models.CharField(max_length=100, blank=True, null=True)
    klub = models.ForeignKey(Klub, blank=True, null=True, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True, choices=REGION)
    datum_rodjenja = models.DateField()
    slika = models.ImageField(upload_to='treneri_profil', default='default.png', blank=True, null=True)
    
    slika_resize = ImageSpecField(
        source='slika', 
        processors=[ResizeToFill(50, 70)],
        format='JPEG',
        options={'quality': 60},
    )

    # uplata = da/ne 

    def __str__(self):
        return str(self.ime)



class UktsTrener(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    licenca = models.CharField(max_length=50, blank=True, null=True)
    boja = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return str(self.prezime)