from django.db import models

from django.core.files.base import ContentFile
from django.conf import settings

from imagekit.models import ImageSpecField
from imagekit.processors import Resize, ResizeToFill, Thumbnail, ResizeToCover, SmartResize, ResizeToFit, ResizeCanvas

from ckeditor_uploader.fields import RichTextUploadingField


class ClanUO(models.Model):
    class Meta:
        verbose_name = 'Clan UO'
        verbose_name_plural = 'Clanovi UO'

    POZICIJA_CHOICES = (
        ('Predsednik', 'Predsednik'),
        ('Generalni sekretar', 'Generalni sekretar'),
        ('Član upravnog odbora', 'Upravni odbor'),
        )


    ime = models.CharField(max_length=100)
    funkcija = models.CharField(max_length=100, choices=POZICIJA_CHOICES, default='uo')
    
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    slika = models.ImageField(upload_to='upravni_odbor/', default='default.png')
    # published to do

    slika_velika = ImageSpecField(
        source='slika', 
        processors=[ResizeToFill(538,324)],
        format='JPEG',
        options={'quality': 60},
    )

    slika_mala = ImageSpecField(
        source='slika', 
        processors=[ResizeToFill(253,303)],
        format='JPEG',
        options={'quality': 60},
    )




    def __str__(self):
        return self.ime








class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class ZivotnoDelo(models.Model):
    class Meta:
        verbose_name = 'Dobitnik Zivotno Delo'
        verbose_name_plural = 'Dobitnici Zivotno Delo'


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)

    body=RichTextUploadingField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    image = models.ImageField(upload_to='zivotno_delo/')

    image_resize = ImageSpecField(
        source='image', 
        processors=[ResizeToFill(538,761)],
        format='JPEG',
        options={'quality': 60},
    )

 
        
    def __str__(self):
        return self.title



class Statut(models.Model):
    class Meta:
        verbose_name = 'Statut'
        verbose_name_plural = 'Statut'


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)

    body=RichTextUploadingField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    image = models.ImageField(upload_to='statut/')
 
        
    def __str__(self):
        return self.title


class Pravilnik(models.Model):
    class Meta:
        verbose_name = 'Pravilnik'
        verbose_name_plural = 'Pravilnik'


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)

    body=RichTextUploadingField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    image = models.ImageField(upload_to='pravilnik/')
 
        
    def __str__(self):
        return self.title


class Kodeks(models.Model):
    class Meta:
        verbose_name = 'Kodeks'
        verbose_name_plural = 'Kodeks'


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)

    body=RichTextUploadingField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    image = models.ImageField(upload_to='kodeks/')
 
        
    def __str__(self):
        return self.title




class Istorijat(models.Model):
    class Meta:
        verbose_name = 'Istorijat'
        verbose_name_plural = 'Istorijat'


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)

    body=RichTextUploadingField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    image = models.ImageField(upload_to='istorijat/')
 
        
    def __str__(self):
        return self.title



class Faq(models.Model):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


    # STATUS_CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    #     )

    pitanje = models.CharField(max_length=250)

    odgovor=RichTextUploadingField()

    # image = models.ImageField(upload_to='faq/', default='default.png')

    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # objects = models.Manager() # The default manager.
    # published = PublishedManager() # Our custom manager.

    # image = models.ImageField(upload_to='istorijat/')
 
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.pitanje