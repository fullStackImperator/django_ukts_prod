from django.contrib import admin

from .models import Knjige, FibaAssist, StrucneTeme, Linkovi, LinkoviPDF

@admin.register(Knjige)
class KnjigeAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'autor', 'godina', 'cover')
    list_filter = ('naslov', 'autor', 'godina', 'cover')
    search_fields = ('naslov', 'autor', 'godina')


@admin.register(FibaAssist)
class FibaAssistAdmin(admin.ModelAdmin):
    list_display = ('broj', 'cover')
    list_filter = ('broj', 'cover')
    search_fields = ('broj', )


@admin.register(StrucneTeme)
class StrucneTemeAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'autor')
    list_filter = ('naslov', 'autor')
    search_fields = ('naslov', 'autor')


@admin.register(Linkovi)
class LinkoviAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    list_filter = ('name', 'link')
    search_fields = ('name', 'link')


@admin.register(LinkoviPDF)
class LinkoviPDFAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )