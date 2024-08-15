import pandas as pd
import numpy as np
import sqlite3
import os

# Caminho para arquivos
diretorio_Script = os.path.dirname(__file__)
caminho_CSV = os.path.join(diretorio_Script, '../database/alunos-ativos-da-pos-graduacao.csv')

# Gerando dataframe
df = pd.read_csv(caminho_CSV, sep=';', usecols=['nome_aluno']).sample(frac=1).reset_index(drop=True)
df = df.rename(columns={'nome_aluno' : 'NOME'})
df['ID'] = range(1, len(df) + 1)
df = df[['ID', 'NOME']]

#Atribuindo sexo considerando nomes com maior frequencia
# df_nomes_frequencia = df['NOME'].map(lambda y: y.split()[0]).value_counts()

nomes_masculinos = ['Lucas', 'João', 'Gabriel', 'Matheus', 'Rafael', 'Guilherme', 'Gustavo', 'Bruno', 'Luiz', 'Paulo', 'Pedro', 'André', 'José', 'Rodrigo', 'Thiago', 'Felipe', 'Daniel', 'Marcelo', 'Eduardo']
nomes_femininos = ['Ana', 'Maria', 'Mariana', 'Bruna', 'Gabriela', 'Camila', 'Fernanda', 'Amanda', 'Aline', 'Leticia', 'Larissa', 'Juliana', 'Jéssica', 'Beatriz', 'Marina']

df['SEXO'] = None
df.loc[df['NOME'].str.split().str[0].isin(nomes_masculinos), 'SEXO'] = 'M'
df.loc[df['NOME'].str.split().str[0].isin(nomes_femininos), 'SEXO'] = 'F'

lista_sexo_aleatorio = np.random.choice(['M', 'F'], size=df['SEXO'].isnull().sum())
df.loc[df['SEXO'].isnull(), 'SEXO'] = lista_sexo_aleatorio  

#Define data de nascimento e idade
df['NASCIMENTO'] = np.random.choice(pd.date_range(start='1910-01-01', end='2019-12-31'), size=len(df))
df['NASCIMENTO'] = pd.to_datetime(df['NASCIMENTO']).dt.date

df['IDADE'] = (pd.Timestamp.now() - pd.to_datetime(df['NASCIMENTO'])).dt.days // 365

#define altura com influencia da idade e sexo
df['ALTURA'] = np.random.randint(120, 210, size=len(df))
df.loc[df['IDADE'] <= 18, 'ALTURA'] -= (25 * (1 - (df['IDADE'] / 18) ** 2 )).round() #quanto menor a idade, maior o decrescimo
df.loc[df['IDADE'] >= 60, 'ALTURA'] -= (30 * ((df['IDADE'] - 60) / (df['IDADE'].max() - 60)) ** 2).round() #quanto maior a idade, maior o decrescimo

df.loc[df['SEXO'] == 'F', 'ALTURA'] -= np.random.randint(1, 8)
df.loc[df['SEXO'] == 'M', 'ALTURA'] += np.random.randint(1, 8)

#define o peso com influencia da idade e sexo
df['PESO'] = np.random.uniform(25.0, 150, size=len(df))

df.loc[df['IDADE'] <= 18, 'PESO'] -= (8 * (1 - (df['IDADE'] / 18) ** 2 )).round(decimals=2)
df.loc[df['IDADE'] >= 60, 'PESO'] -= (15 * ((df['IDADE'] - 60) / (df['IDADE'].max() - 60)) ** 2).round(decimals=2)

df.loc[df['SEXO'] == 'F', 'PESO'] -= (df['PESO'] * 0.05).round(decimals=2)
df.loc[df['SEXO'] == 'M', 'PESO'] += (df['PESO'] * 0.05).round(decimals=2)

df['PESO'] = np.round(df['PESO'], decimals=2)

# define pressao arterial
df['PRESSAO_SISTOLICA'] = 10 * np.random.randint(5, 23, size=len(df))
df['PRESSAO_DIASTOLICA'] = 10 * np.random.randint(3, (df['PRESSAO_SISTOLICA']/10), size=len(df))

df.loc[df['IDADE'] <= 18, ['PRESSAO_SISTOLICA', 'PRESSAO_DIASTOLICA']] -= (10 * np.random.randint(1, 4))

# define glicemia com aumento na terceira idade
df['GLICEMIA'] = 5 * np.random.randint(8, 44, size=len(df))
df.loc[df['IDADE'] >= 60, 'GLICEMIA'] += 5 * np.random.randint(1, 4)

# Gera um valor de frequencia cardiaca com influencia da idade
df['FREQUENCIA_CARDIACA'] = np.random.randint(30, 210, size=len(df))

df.loc[df['IDADE'] <= 18, 'FREQUENCIA_CARDIACA'] += (np.random.randint(20, 40) * (1 - (df['IDADE'] / 18) ** 2 )).round()
df.loc[df['IDADE'] >= 60, 'FREQUENCIA_CARDIACA'] += (np.random.randint(10, 30) * ((df['IDADE'] - 60) / (df['IDADE'].max() - 60)) ** 2).round()

print(df)

caminho_Database = os.path.join(diretorio_Script, '../mysite/db.sqlite3')

with sqlite3.connect(caminho_Database) as conexao:

    cursor = conexao.cursor()

    cursor.execute('DROP TABLE IF EXISTS HealthHub_pacientes')

    cursor.execute('''
        CREATE TABLE HealthHub_pacientes (
            ID INTEGER PRIMARY KEY NOT NULL,
            NOME TEXT NOT NULL,
            SEXO TEXT NOT NULL,
            NASCIMENTO DATE NOT NULL,
            IDADE INTEGER NOT NULL,
            ALTURA INTEGER NOT NULL,
            PESO REAL NOT NULL,
            PRESSAO_SISTOLICA INTEGER NOT NULL,
            PRESSAO_DIASTOLICA INTEGER NOT NULL,
            GLICEMIA INTEGER NOT NULL,
            FREQUENCIA_CARDIACA INTEGER NOT NULL
        )
    ''')

    df.to_sql('HealthHub_pacientes', conexao, if_exists='append', index=False)

"""
df['circunferencia-cintura']
df['diabetes']
df['doenca-cronica']
df['tabagismo']
df['colesterol']
df['funcao-renal']
df['alergia']
df['duracao-sono']"""