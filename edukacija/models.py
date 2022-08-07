from django.db import models

from django.core.files.base import ContentFile
from django.conf import settings



class Knjige(models.Model):
    class Meta:
        verbose_name = 'Knjiga'
        verbose_name_plural = 'Knjige'


    naslov = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, default='')
    godina = models.IntegerField()
    pdf = models.FileField(upload_to='knjige/pdf')
    cover = models.ImageField(upload_to='knjige/covers/', default='all_domaci.jpeg')
    # published to do


    def __str__(self):
        return self.naslov