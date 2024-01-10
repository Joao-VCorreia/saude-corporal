from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, default='')
    sobrenome = models.CharField(max_length=100, default='')
    nascimento = models.DateField(default='2000-01-01')
    altura = models.FloatField(default=0.0)
    peso = models.FloatField(default=0.0)
    pressao_arterial = models.CharField(max_length=20, default='')
    glicemia = models.FloatField(default=0.0)
    frequencia_cardiaca = models.IntegerField(default=0)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M')

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    