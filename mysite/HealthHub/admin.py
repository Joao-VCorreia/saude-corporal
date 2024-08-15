from django.contrib import admin
from .models import HealthhubPacientes

@admin.register(HealthhubPacientes)
class HealthhubPacientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'nascimento', 'idade', 'altura', 'peso', 'pressao_sistolica', 'pressao_diastolica', 'glicemia', 'frequencia_cardiaca')

# Register your models here.
