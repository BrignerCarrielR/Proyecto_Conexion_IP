from django.contrib import admin

from monitoreo.models import Switch


# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['nombre','ip','bloque']
    search_fields = ['nombre']
    list_per_page = 5

admin.site.register(Switch)