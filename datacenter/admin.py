from django.contrib import admin

from datacenter import models

# Register your models here.
@admin.register(models.Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = 'nep','ponta_a', 'ponta_b','description','group'
    ordering = '-id',
    search_fields = 'net', 'ponta_a', 'ponta_b', 'description', '' 
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'ponta_a', 'ponta_b', 'description',
    list_display_links = 'nep','group'


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    search_fields = 'name', 'description',