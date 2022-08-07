from django.contrib import admin

from .models import Klinike, Photo#, BaseGallery, GalleryImage #, Album, Photo
from .forms import UploadForm

@admin.register(Klinike)
class KlinikeAdmin(admin.ModelAdmin):
    list_display = ('tip', 'predavac', 'godina', 'link', 'cover')
    list_filter = ('tip', 'predavac', 'godina', 'link', 'cover')
    search_fields = ('tip', 'predavac', 'godina', 'link')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('tip', 'godina', 'slika', 'naslov')
    list_filter = ('tip', 'godina', 'slika', 'naslov')
    search_fields = ('tip', 'godina', 'naslov')


# @admin.register(BaseGallery)
# class BaseGalleryAdmin(admin.ModelAdmin):
#     model = BaseGallery

# @admin.register(GalleryImage)
# class GalleryImageAdmin(admin.ModelAdmin):
#     model = GalleryImage

# class PhotoAdmin(admin.StackedInline):
#     model = Photo

# @admin.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#     inlines = [PhotoAdmin]

#     list_display = ('tip', 'godina')
#     list_filter = ('tip', 'godina')
#     search_fields = ('tip', 'godina')

# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
#     pass


