from django.db import models
import os


from django.core.files.base import ContentFile
from django.conf import settings
from zipfile import ZipFile

from ckeditor_uploader.fields import RichTextUploadingField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# from orderable.models import Orderable


class Klinike(models.Model):
    class Meta:
        verbose_name = 'Klinika video'
        verbose_name_plural = 'Klinike video'
        ordering = ('-godina',)

    # KLINIKA_CHOICES = (
    #     ('bcb', 'Beogradska Kosarkaska Klinika'),
    #     ('td', 'Trenerski Dani'),
    #     )
    # tip = models.CharField(max_length=50, choices=KLINIKA_CHOICES, default='bcb')
    predavac = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default='')
    godina = models.IntegerField()
    # owner = models.CharField(max_length=100)
    link = models.URLField(max_length = 200)
    cover = models.ImageField(upload_to='klinike/covers/', default='all_domaci.jpeg')
    # cover_same = ImageSpecField(source='cover',
    #                                   processors=[ResizeToFill(300, 500)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})



    def __str__(self):
        return self.predavac


class TrenerskiDani(models.Model):
    class Meta:
        verbose_name = 'Trenerski Dan video'
        verbose_name_plural = 'Trenerski Dani video'

    predavac = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default='')
    godina = models.IntegerField()
    # owner = models.CharField(max_length=100)
    link = models.URLField(max_length = 200)
    cover = models.ImageField(upload_to='klinike/covers/', default='all_domaci.jpeg')
    # published to do


    def __str__(self):
        return self.predavac

# def slika_upload_location(instance, filename):
#     slika_tip = instance.tip
#     file_name = filename.lower().replace(" ", "-")
#     return "klinike/{}/{}".format(slika_tip, file_name)


class BCB(models.Model):
    class Meta:
        verbose_name = 'bcb'
        verbose_name_plural = 'bcb'

    godina = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return self.godina


class SlikeBCB(models.Model):
    klinika = models.ForeignKey(BCB, on_delete=models.SET_NULL, null=True, blank=True)
    slika = models.ImageField(upload_to='bcb/slike/', null=False, blank=False)



class TD(models.Model):
    class Meta:
        verbose_name = 'td'
        verbose_name_plural = 'td'

    godina = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return self.godina


class SlikeTD(models.Model):
    trenerski_dan = models.ForeignKey(TD, on_delete=models.SET_NULL, null=True, blank=True)
    slika = models.ImageField(upload_to='td/slike/', null=False, blank=False)




class BCB_Promocija(models.Model):
    class Meta:
        verbose_name = 'BCB promocija i najava'
        verbose_name_plural = 'BCB promocija i najava'
        ordering = ('-godina',)

    godina = models.CharField(max_length=4, null=False, blank=False)
    datum_odrzavanja = models.DateField(null=True, blank=True)
    promo_video = models.URLField(max_length = 200, blank=True)
    slika_landing_page = models.ImageField(upload_to='bcb_promo/klinika/', default='all_domaci.jpeg')
    slika_landing_page_scale = ImageSpecField(source='slika_landing_page',
                                      processors=[ResizeToFill( 530, 620 )],
                                      format='JPEG',
                                      options={'quality': 80})
    poruka_landing_page = RichTextUploadingField()
    poruka_promo_page = RichTextUploadingField()

    def __str__(self):
        return self.godina


class BCB_Predavac(models.Model):
    class Meta:
        verbose_name = 'BCB Predavač promocija'
        verbose_name_plural = 'BCB Predavači promocija'

    bcb_promocija = models.ForeignKey(BCB_Promocija, on_delete=models.SET_NULL, null=True, blank=True)
    predavac = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default='')
    slika_promo_page = models.ImageField(upload_to='bcb_promo/predavaci/', default='all_domaci.jpeg')
    slika_promo_slider = models.ImageField(upload_to='bcb_promo/predavaci/', default='all_domaci.jpeg')

    def __str__(self):
        return self.predavac