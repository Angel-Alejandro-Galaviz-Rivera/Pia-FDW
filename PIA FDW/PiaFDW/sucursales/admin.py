from django.contrib import admin
from .models import Sucursales
# Register your models here.
class SucursalesAdmin(admin.ModelAdmin):
    list_display = ('Id_Sucursal','Nombre','Ubicacion','Numero_de_Telefono')
    ordering = ('Ubicacion','Numero_de_Telefono')
    search_fields = ('Id_Sucursal','Nombre')
  
admin.site.register(Sucursales,SucursalesAdmin)