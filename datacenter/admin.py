from django.contrib import admin

from datacenter import models

# Register your models here.
@admin.register(models.Cable)
class CableAdmin(admin.ModelAdmin):
    list_display = 'nep','ponta_a', 'ponta_b','description','group_dev','dev_a','dev_b',
    ordering = '-id',
    search_fields = 'nep', 'ponta_a', 'ponta_b', 'description', 'dev_a', 'dev_b', 
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'ponta_a', 'ponta_b', 'description','dev_a', 'dev_b',
    list_display_links = 'nep','group_dev'

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    search_fields = 'name', 'description',

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = 'group_dev',
    ordering = '-id',
    search_fields = 'group_dev',
