from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class resourcecliente(resources.ModelResource):
    class Meta:
        model = cliente

class admincliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre','Dpi','Edad','direccion']
    resource_class = resourcecliente

admin.site.register(cliente,admincliente)


class resourcemascota(resources.ModelResource):
    class Meta:
        model = mascota

class adminmascota(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['tipo']
    list_display = ['tipo','raza','edad','vacunas','estado']
    resource_class = resourcemascota


admin.site.register(mascota, adminmascota)

class resourcecita(resources.ModelResource):
    class Meta:
        model = cita

class admincita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha_y_hora']
    resource_class = resourcecita

admin.site.register(cita, admincita)
