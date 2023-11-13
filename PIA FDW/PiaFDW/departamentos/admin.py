from django.contrib import admin
from .models import Departamentos
# Register your models here.
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('Id_Departamento','Nombre','Descripcion','Responsable')
    ordering = ('Descripcion','Responsable')
    search_fields = ('Id_Departamento','Nombre')
    
admin.site.register(Departamentos,DepartamentosAdmin)