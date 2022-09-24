from django.contrib import admin

from .models import Klinike, TrenerskiDani, BCB_Promocija, BCB_Predavac, BCB, SlikeBCB #, BaseGallery, GalleryImage #, Album, Photo


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

@admin.register(BCB_Promocija)
class BCB_PromocijaAdmin(admin.ModelAdmin):
    list_display = ('godina', 'datum_odrzavanja', 'promo_video', 'slika_landing_page', 'poruka_landing_page', 'poruka_promo_page')
    # search_fields = ('predavac', 'godina', 'tema')

@admin.register(BCB_Predavac)
class BCB_PredavacAdmin(admin.ModelAdmin):
    list_display = ('predavac', 'tema', 'slika_promo_page', 'slika_promo_slider')
    # search_fields = ('predavac', 'godina', 'tema')


# admin.site.register(BCB)
# admin.site.register(SlikeBCB)



