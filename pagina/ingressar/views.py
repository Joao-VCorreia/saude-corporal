from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.db import connection
from .models import Paciente

def login_usuario(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('/cadastro/')
        else:
            return HttpResponse('Nome ou senha invalidos')


def cadastro(request):
    if request.user.is_authenticated:
        return render(request, 'cadastro.html')
    
    return redirect(login_usuario)


def cadastrar_paciente(request):

    if request.method == 'POST':

        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        nascimento = request.POST['nascimento']
        altura = request.POST['altura']
        peso = request.POST['peso']
        pressao_arterial = request.POST['pressao_arterial']
        glicemia = request.POST['glicemia']
        frequencia_cardiaca = request.POST['frequencia_cardiaca']  
        sexo = request.POST['sexo']

        # Criar e salvar um novo objeto Paciente
        paciente = Paciente(
            nome=nome.upper(),
            sobrenome=sobrenome.upper(),
            nascimento=nascimento,
            altura=altura,
            peso=peso,
            pressao_arterial=pressao_arterial,
            glicemia=glicemia,
            frequencia_cardiaca=frequencia_cardiaca,
            sexo=sexo
        )
        paciente.save()

        # Redirecionar para alguma página de confirmação ou outra página desejada
        return redirect(listar_pacientes)

    return render(request, 'cadastro.html')

def listar_pacientes(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.all().order_by('id')[:15]
        return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
    
    return redirect(login_usuario)

def pesquisar_pacientes(request):
    if request.user.is_authenticated:
        results = []
        search_term = request.GET.get('pesquisa', '')

        if search_term:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''
                    SELECT * FROM Pacientes
                    WHERE nome LIKE %s
                    ORDER BY nome asc
                    LIMIT 15;
                    ''',
                    [search_term + '%']
                )
                columns = [col[0] for col in cursor.description]
                results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return render(request, 'lista_pacientes.html', {'search_term': search_term, 'results': results})
        
        else:
            return redirect(listar_pacientes)

    return redirect(login_usuario)
