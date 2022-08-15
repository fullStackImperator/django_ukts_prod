from django.contrib import admin

from .models import ClanUO, ZivotnoDelo, Statut, Pravilnik, Kodeks, Istorijat, Faq


@admin.register(ClanUO)
class ClanUOAdmin(admin.ModelAdmin):
    list_display = ('ime', 'funkcija', 'linkedin', 'twitter', 'facebook', 'instagram')
    list_filter = ('ime', 'funkcija', 'linkedin', 'twitter', 'facebook', 'instagram')
    search_fields = ('ime', 'funkcija')


@admin.register(ZivotnoDelo)
class ZivotnoDeloAdmin(admin.ModelAdmin): 
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')

@admin.register(Statut)
class StatutAdmin(admin.ModelAdmin): 
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')


@admin.register(Pravilnik)
class PravilnikAdmin(admin.ModelAdmin): 
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')

@admin.register(Kodeks)
class KodeksAdmin(admin.ModelAdmin): 
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')


@admin.register(Istorijat)
class IstorijatAdmin(admin.ModelAdmin): 
    list_display = ('title', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin): 
    list_display = ('pitanje', 'odgovor')
    list_filter = ('pitanje', 'odgovor')
    search_fields = ('pitanje', 'odgovor')