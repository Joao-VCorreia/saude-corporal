from django.db import models

class HealthhubPacientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.TextField(db_column='NOME')
    sexo = models.TextField(db_column='SEXO')
    nascimento = models.DateField(db_column='NASCIMENTO')
    idade = models.IntegerField(db_column='IDADE')
    altura = models.IntegerField(db_column='ALTURA')
    peso = models.FloatField(db_column='PESO')
    pressao_sistolica = models.IntegerField(db_column='PRESSAO_SISTOLICA')
    pressao_diastolica = models.IntegerField(db_column='PRESSAO_DIASTOLICA')
    glicemia = models.IntegerField(db_column='GLICEMIA')
    frequencia_cardiaca = models.IntegerField(db_column='FREQUENCIA_CARDIACA')

    class Meta:
        managed = False
        db_table = 'HealthHub_pacientes'

    def __str__(self):
        return f'{self.nome} (ID: {self.id})'