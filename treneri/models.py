from django.db import models

# Create your models here.

class Klub(models.Model):
    ime_kluba = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ime_kluba

class Trener(models.Model):
    ime = models.CharField(max_length=100, blank=True, null=True)
    licenca = models.CharField(max_length=100, blank=True, null=True)
    klub = models.ForeignKey(Klub, blank=True, null=True, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    
    # uplata = da/ne 