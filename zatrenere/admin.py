from django.contrib import admin

from .models import Planeri, Lekarski, Uplatnice

@admin.register(Planeri)
class PlaneriAdmin(admin.ModelAdmin):
    list_display = ('ime', 'file', 'cover')
    list_filter = ('ime', 'file', 'cover')
    search_fields = ('ime', 'file')


@admin.register(Lekarski)
class LekarskiAdmin(admin.ModelAdmin):
    list_display = ('ime', 'file', 'cover')
    list_filter = ('ime', 'file', 'cover')
    search_fields = ('ime', 'file')


@admin.register(Uplatnice)
class UplatniceAdmin(admin.ModelAdmin):
    list_display = ('ime', 'file', 'cover')
    list_filter = ('ime', 'file', 'cover')
    search_fields = ('ime', 'file')