from django.db import models

class HealthhubPacientes(models.Model):
    nome = models.TextField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    nascimento = models.TextField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    pressao_arterial_sistolica = models.IntegerField(blank=True, null=True)
    pressao_arterial_diastolica = models.IntegerField(blank=True, null=True)
    glicemia = models.IntegerField(blank=True, null=True)
    frequencia_cardiaca = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HealthHub_pacientes'