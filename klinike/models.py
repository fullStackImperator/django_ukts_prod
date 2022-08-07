from django.db import models
import os


from django.core.files.base import ContentFile
from django.conf import settings
from zipfile import ZipFile

# from orderable.models import Orderable


class Klinike(models.Model):
    class Meta:
        verbose_name = 'Klinika'
        verbose_name_plural = 'Klinike'

    KLINIKA_CHOICES = (
        ('bcb', 'Beogradska Kosarkaska Klinika'),
        ('td', 'Trenerski Dani'),
        )
    tip = models.CharField(max_length=50, choices=KLINIKA_CHOICES, default='bcb')
    predavac = models.CharField(max_length=100)
    tema = models.CharField(max_length=100, default='')
    godina = models.IntegerField()
    # owner = models.CharField(max_length=100)
    link = models.URLField(max_length = 200)
    cover = models.ImageField(upload_to='klinike/covers/', default='all_domaci.jpeg')
    # published to do


    def __str__(self):
        return self.predavac


def slika_upload_location(instance, filename):
    slika_tip = instance.tip
    file_name = filename.lower().replace(" ", "-")
    return "klinike/{}/{}".format(slika_tip, file_name)



class Photo(models.Model):
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
    
    # category = models.ForeignKey(
    #     Category, on_delete=models.SET_NULL, null=True, blank=True)
    KLINIKA_CHOICES = (
        ('bcb', 'Beogradska Kosarkaska Klinika'),
        ('td', 'Trenerski Dani'),
        )
    tip = models.CharField(max_length=50, choices=KLINIKA_CHOICES, default='bcb')
    godina = models.CharField(max_length=4)

    slika = models.ImageField(upload_to=slika_upload_location)

# slika = models.ImageField(upload_to='klinike/bcb/galerija/', null=False, blank=False)
    # slika = models.ImageField()
    # if tip == 'bcb':
    #     slika = models.ImageField(upload_to='klinike/bcb/galerija/', null=False, blank=False)
    # elif tip == 'td':
    #     slika = models.ImageField(upload_to='klinike/td/galerija/', null=False, blank=False)
    # else:
    #     pass

    naslov = models.CharField(max_length=50, blank=True)

    

    def __str__(self):
        return self.naslov


# class Category(models.Model):
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

#     user = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(max_length=100, null=False, blank=False)

#     def __str__(self):
#         return self.name


# class Photo(models.Model):
#     class Meta:
#         verbose_name = 'Photo'
#         verbose_name_plural = 'Photos'
    
#     category = models.ForeignKey(
#         Category, on_delete=models.SET_NULL, null=True, blank=True)
#     image = models.ImageField(upload_to='klinike/bcb/galerija/', null=False, blank=False)
#     description = models.TextField()

#     def __str__(self):
#         return self.description






# def slika_upload_location(instance, filename):
#     slika_tip = instance.slika.tip
#     file_name = filename.lower().replace(" ", "-")
#     return "slike/{}/{}".format(slika_tip, file_name)

# class Case(models.Model):
#     class Meta:
#         verbose_name = 'Album'
#         verbose_name_plural = 'Albumi'


#     KLINIKA_CHOICES = (
#     ('bcb', 'Beogradska Kosarkaska Klinika'),
#     ('td', 'Trenerski Dani'),
#     )

#     tip = models.CharField(max_length=50, choices=KLINIKA_CHOICES, default='---')
#     godina = models.CharField(max_length=4)
#     # naslov = models.CharField(max_length=50, null = True, blank = True)

  
# class CaseFile(models.Model):
#     class Meta:
#         verbose_name = 'Slika'
#         verbose_name_plural = 'Slike'

#     slika = models.ForeignKey(Case, on_delete=models.CASCADE) # When a Case is deleted, upload models are also deleted
#     file = models.ImageField(upload_to=slika_upload_location, null = True, blank = True)




# class BaseGallery(models.Model):
#     zip_import = models.FileField(blank=True, upload_to="galleries")

#     KLINIKA_CHOICES = (
#         ('bcb', 'Beogradska Kosarkaska Klinika'),
#         ('td', 'Trenerski Dani'),
#         )
#     tip = models.CharField(max_length=50, choices=KLINIKA_CHOICES, default='bcb')
#     godina = models.CharField(max_length=4)

#     def save(self, delete_zip_import=True, *args, **kwargs):
#         """
#         If a zip file is uploaded, extract any images from it and add
#         them to the gallery, before removing the zip file.
#         """
#         super(BaseGallery, self).save(*args, **kwargs)
#         if self.zip_import:
#             zip_file = ZipFile(self.zip_import)
#             for name in zip_file.namelist():
#                 data = zip_file.read(name)
#                 try:
#                     from PIL import Image
#                     image = Image.open(BytesIO(data))
#                     image.load()
#                     image = Image.open(BytesIO(data))
#                     image.verify()
#                 except ImportError:
#                     pass
#                 except:
#                     continue
#                 name = os.path.split(name)[1]
#                 # You now have an image which you can save
#                 path = os.path.join(settings.MEDIA_ROOT, "galleries", 
#                                         native(str(name, errors="ignore")))
#                 saved_path = default_storage.save(path, ContentFile(data))
#                 self.images.create(file=saved_path)
#             if delete_zip_import:
#                 zip_file.close()
#                 self.zip_import.delete(save=True)


# class GalleryImage(Orderable):
#     gallery = models.ForeignKey(BaseGallery, related_name="images", on_delete=models.CASCADE)
#     file = models.ImageField(upload_to="galleries")


