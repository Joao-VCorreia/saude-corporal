# Generated by Django 5.0.6 on 2024-08-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthhubPacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, null=True)),
                ('sexo', models.TextField(blank=True, null=True)),
                ('nascimento', models.TextField(blank=True, null=True)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('altura', models.IntegerField(blank=True, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('pressao_arterial_sistolica', models.IntegerField(blank=True, null=True)),
                ('pressao_arterial_diastolica', models.IntegerField(blank=True, null=True)),
                ('glicemia', models.IntegerField(blank=True, null=True)),
                ('frequencia_cardiaca', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'HealthHub_pacientes',
                'managed': False,
            },
        ),
    ]
