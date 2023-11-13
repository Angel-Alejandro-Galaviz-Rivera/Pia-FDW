from django.contrib import admin
from .models import Ambulancias
# Register your models here.
class AmbulanciasAdmin(admin.ModelAdmin):
    list_display = ('Id_Ambulancia','Marca','Modelo','Estado')
    ordering = ('Modelo','Estado')
    search_fields = ('Id_Ambulancia','Marca')

admin.site.register(Ambulancias,AmbulanciasAdmin)