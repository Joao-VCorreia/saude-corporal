import pandas as pd
import numpy as np
import sqlite3
import os

# Caminho para arquivos
diretorio_Script = os.path.dirname(__file__)
caminho_CSV = os.path.join(diretorio_Script, '../database/alunos-ativos-da-pos-graduacao.csv')

# Gerando dataframe
df = pd.read_csv(caminho_CSV, sep=';', usecols=['nome_aluno']).sample(frac=1).reset_index(drop=True)
df = df.rename(columns={'nome_aluno' : 'nome'})

#Atribuindo sexo considerando nomes com maior frequencia
# df_nomes_frequencia = df['nome'].map(lambda y: y.split()[0]).value_counts()

nomes_masculinos = ['Lucas', 'João', 'Gabriel', 'Matheus', 'Rafael', 'Guilherme', 'Gustavo', 'Bruno', 'Luiz', 'Paulo', 'Pedro', 'André', 'José', 'Rodrigo', 'Thiago', 'Felipe', 'Daniel', 'Marcelo', 'Eduardo']
nomes_femininos = ['Ana', 'Maria', 'Mariana', 'Bruna', 'Gabriela', 'Camila', 'Fernanda', 'Amanda', 'Aline', 'Leticia', 'Larissa', 'Juliana', 'Jéssica', 'Beatriz', 'Marina']

df['sexo'] = None
df.loc[df['nome'].str.split().str[0].isin(nomes_masculinos), 'sexo'] = 'M'
df.loc[df['nome'].str.split().str[0].isin(nomes_femininos), 'sexo'] = 'F'

lista_sexo_aleatorio = np.random.choice(['M', 'F'], size=df['sexo'].isnull().sum())
df.loc[df['sexo'].isnull(), 'sexo'] = lista_sexo_aleatorio  

#Define data de nascimento e idade
df['nascimento'] = None
df.loc[df['nascimento'].isnull(), 'nascimento'] = np.random.choice(pd.date_range(start='1910-01-01', end='2019-12-31'), size=len(df))
df['nascimento'] = pd.to_datetime(df['nascimento'])

df['idade'] = (pd.Timestamp.now() - pd.to_datetime(df['nascimento'])).dt.days // 365

#define altura com influencia da idade e sexo
df['altura'] = np.random.randint(120, 210, size=len(df))
df.loc[df['idade'] <= 18, 'altura'] -= (25 * (1 - (df['idade'] / 18) ** 2 )).round() #quanto menor a idade, maior o decrescimo
df.loc[df['idade'] >= 60, 'altura'] -= (30 * ((df['idade'] - 60) / (df['idade'].max() - 60)) ** 2).round() #quanto maior a idade, maior o decrescimo

df.loc[df['sexo'] == 'F', 'altura'] -= np.random.randint(1, 8)
df.loc[df['sexo'] == 'M', 'altura'] += np.random.randint(1, 8)

#define o peso com influencia da idade e sexo
df['peso'] = np.round(np.random.uniform(25.0, 150, size=len(df)), decimals=2)
df.loc[df['idade'] <= 18, 'peso'] -= (8 * (1 - (df['idade'] / 18) ** 2 )).round(decimals=2)
df.loc[df['idade'] >= 60, 'peso'] -= (15 * ((df['idade'] - 60) / (df['idade'].max() - 60)) ** 2).round(decimals=2)

df.loc[df['sexo'] == 'F', 'peso'] -= (df['peso'] * 0.05).round(decimals=2)
df.loc[df['sexo'] == 'M', 'peso'] += (df['peso'] * 0.05).round(decimals=2)

# define pressao arterial
df['pressao_arterial_sistolica'] = 10 * np.random.randint(5, 23, size=len(df))
df['pressao_arterial_diastolica'] = 10 * np.random.randint(3, (df['pressao_arterial_sistolica']/10), size=len(df))

df.loc[df['idade'] <= 18, ['pressao_arterial_sistolica', 'pressao_arterial_diastolica']] -= (10 * np.random.randint(1, 4))

# define glicemia com aumento na terceira idade
df['glicemia'] = 5 * np.random.randint(8, 44, size=len(df))
df.loc[df['idade'] >= 60, 'glicemia'] += 5 * np.random.randint(1, 4)

# Gera um valor de frequencia cardiaca com influencia da idade
df['frequencia_cardiaca'] = np.random.randint(30, 210, size=len(df))

df.loc[df['idade'] <= 18, 'frequencia_cardiaca'] += (np.random.randint(20, 40) * (1 - (df['idade'] / 18) ** 2 )).round()
df.loc[df['idade'] >= 60, 'frequencia_cardiaca'] += (np.random.randint(10, 30) * ((df['idade'] - 60) / (df['idade'].max() - 60)) ** 2).round()

caminho_Database = os.path.join(diretorio_Script, '../mysite/db.sqlite3')
with sqlite3.connect(caminho_Database) as conexao:
    df.to_sql('HealthHub_pacientes', conexao, if_exists='replace', index=False)

"""
df['circunferencia-cintura']
df['diabetes']
df['doenca-cronica']
df['tabagismo']
df['colesterol']
df['funcao-renal']
df['alergia']
df['duracao-sono']"""