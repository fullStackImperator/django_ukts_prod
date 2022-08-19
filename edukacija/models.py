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


class FibaAssist(models.Model):
    class Meta:
        verbose_name = 'Fiba Assist'
        verbose_name_plural = 'Fiba Assist'

    broj = models.CharField(max_length=3)
    pdf = models.FileField(upload_to='FIBA/pdf')
    cover = models.ImageField(upload_to='FIBA/covers/', default='all_domaci.jpeg')
    # published to do


    def __str__(self):
        return self.broj


class StrucneTeme(models.Model):
    class Meta:
        verbose_name = 'Strucne Teme'
        verbose_name_plural = 'Strucne Teme'

    autor = models.CharField(max_length=70)
    naslov = models.CharField(max_length=150)
    pdf = models.FileField(upload_to='strucne')
    # published to do


    def __str__(self):
        return self.naslov



class Linkovi(models.Model):
    class Meta:
        verbose_name = 'Linkovi'
        verbose_name_plural = 'Linkovi'


    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    cover = models.ImageField(upload_to='linkovi/', default='all_domaci.jpeg')

    # godina = models.IntegerField()
    # pdf = models.FileField(upload_to='knjige/pdf')
    # cover = models.ImageField(upload_to='knjige/covers/', default='all_domaci.jpeg')
    # published to do


    def __str__(self):
        return self.name


class LinkoviPDF(models.Model):
    class Meta:
        verbose_name = 'Linkovi PDF'
        verbose_name_plural = 'Linkovi PDF'

    name = models.CharField(max_length=150)
    pdf = models.FileField(upload_to='linkovi/pdf')
    cover = models.ImageField(upload_to='linkovi/cover', default='link_cover3.png')

    # published to do


    def __str__(self):
        return self.name