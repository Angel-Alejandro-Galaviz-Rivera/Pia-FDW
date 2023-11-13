from django.contrib import admin
from .models import Medicos
# Register your models here.
class MedicosAdmin(admin.ModelAdmin):
    list_display = ('Id_Medico','Nombre_Completo','Especialidad','Numero_de_Telefono')
    ordering = ('Especialidad','Numero_de_Telefono')
    search_fields = ('Id_Medico','Nombre_Completo')

admin.site.register(Medicos,MedicosAdmin)