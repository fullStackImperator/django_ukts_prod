from django.contrib import admin

from .models import Knjige

@admin.register(Knjige)
class EdukacijaAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'autor', 'godina', 'cover')
    list_filter = ('naslov', 'autor', 'godina', 'cover')
    search_fields = ('naslov', 'autor', 'godina')