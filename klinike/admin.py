from django.contrib import admin

from .models import Klinike, TrenerskiDani, BCB, SlikeBCB #, BaseGallery, GalleryImage #, Album, Photo


@admin.register(Klinike)
class KlinikeAdmin(admin.ModelAdmin):
    list_display = ('predavac', 'godina', 'tema', 'cover')
    list_filter = ('predavac', 'godina', 'tema', 'cover')
    search_fields = ('predavac', 'godina', 'tema')


@admin.register(TrenerskiDani)
class TrenerskiDaniAdmin(admin.ModelAdmin):
    list_display = ('predavac', 'godina', 'tema', 'cover')
    list_filter = ('predavac', 'godina', 'tema', 'cover')
    search_fields = ('predavac', 'godina', 'tema')



# admin.site.register(BCB)
# admin.site.register(SlikeBCB)



