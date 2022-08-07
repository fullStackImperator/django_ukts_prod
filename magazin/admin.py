from django.contrib import admin

from .models import Files

@admin.register(Files)
class MagazinAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdf', 'cover')
    list_filter = ('name', 'pdf', 'cover')
    search_fields = ('name', 'pdf')