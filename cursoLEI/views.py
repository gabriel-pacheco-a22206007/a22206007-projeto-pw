from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from cursoLEI.models import Curso, Disciplina, Projeto, Area_Cientifica, Linguagem_Programacao, Docente
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def lista_docente_view(request):
    docentes = Docente.objects.all()
    return render(request, 'cursoLEI/lista_docente.html', {'docentes': docentes})

@login_required
def remover_docente_view(request, docente_id):
    docente = get_object_or_404(Docente, pk=docente_id)
    docente.delete()
    return redirect('cursoLEI:lista_docente')

@login_required
def criar_docente_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        docente = Docente(nome=nome)
        docente.save()
        return redirect('cursoLEI:lista_docente')

    return render(request, 'cursoLEI/criar_docente.html')

@login_required
def remover_lingua_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    linguagens = Linguagem_Programacao.objects.all()
    if request.method == 'POST':
        linguagens_ids = request.POST.getlist('linguagens')

        if linguagens_ids:
            linguagens_selecionadas = Linguagem_Programacao.objects.filter(id__in=linguagens_ids)
            linguagens_selecionadas.delete()

        return redirect('cursoLEI:projeto_disciplina', projeto_nome=projeto.nome)

    return render(request, 'cursoLEI/remover_lingua.html', {'projeto': projeto, 'linguagens': linguagens})

@login_required
def criar_lingua_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        lingua = Linguagem_Programacao(nome=nome)
        lingua.save()
        return redirect('cursoLEI:projeto_disciplina', projeto_nome=projeto.nome)

    return render(request, 'cursoLEI/criar_lingua.html', {'projeto': projeto})

@login_required
def editar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    linguagens = Linguagem_Programacao.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        conceitos = request.POST.get('conceitos')
        tecnologias = request.POST.get('tecnologias')
        foto = request.FILES.get('foto')
        video = request.POST.get('video')
        gitLink = request.POST.get('gitLink')
        linguagens_ids = request.POST.getlist('linguagens')

        projeto.nome=nome
        projeto.descricao=descricao
        projeto.conceitos=conceitos
        projeto.tecnologias=tecnologias
        projeto.foto=foto
        projeto.video=video
        projeto.gitLink=gitLink
        projeto.save()

        if linguagens_ids:
            linguagens_selecionadas = Linguagem_Programacao.objects.filter(id__in=linguagens_ids)
            projeto.linguagens.set(linguagens_selecionadas)

        projeto.save()
        return redirect('cursoLEI:projeto_disciplina', projeto_nome=projeto.nome)
    return render(request,'cursoLEI/editar_projeto.html', {'projeto': projeto, 'linguagens': linguagens })

@login_required
def remover_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    disciplina = projeto.disciplina
    projeto.delete()
    return redirect('cursoLEI:disciplina_lista', disciplina_nome = disciplina.nome)

@login_required
def criar_projeto_view(request, disciplina_id):
    linguagens = Linguagem_Programacao.objects.all()
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        conceitos = request.POST.get('conceitos')
        tecnologias = request.POST.get('tecnologias')
        foto = request.FILES.get('foto')
        video = request.POST.get('video')
        gitLink = request.POST.get('gitLink')
        linguagens_ids = request.POST.getlist('linguagens')

        projeto = Projeto(nome=nome, descricao=descricao, conceitos=conceitos, tecnologias=tecnologias, foto=foto, video=video, gitLink=gitLink, disciplina=disciplina)
        projeto.save()

        if linguagens_ids:
            linguagens_selecionadas = Linguagem_Programacao.objects.filter(id__in=linguagens_ids)
            projeto.linguagens.set(linguagens_selecionadas)

        return redirect('cursoLEI:disciplina_lista', disciplina_nome=disciplina.nome)

    return render(request, 'cursoLEI/criar_projeto.html', {'linguagens': linguagens, 'disciplina': disciplina})

@login_required
def remover_area_pagina_view(request):
    areas =  Area_Cientifica.objects.all()
    if request.method == 'POST':
        area_id = request.POST.get('area')
        return redirect('cursoLEI:remover_area', area_id=area_id)

    return render(request, 'cursoLEI/remover_area.html', {'areas': areas})

@login_required
def remover_area_view(request, area_id):
    area = get_object_or_404(Area_Cientifica, pk=area_id)
    area.delete()
    return redirect('cursoLEI:remover_area_pagina')

@login_required
def criar_area_criar_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        area = Area_Cientifica(nome=nome)
        area.save()
        return redirect('cursoLEI:criar_disciplina')

    return render(request, 'cursoLEI/criar_area.html')

@login_required
def criar_area_editar_view(request, disciplina_id):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        area = Area_Cientifica(nome=nome)
        area.save()
        return redirect('cursoLEI:editar_disciplina', disciplina_id=disciplina_id)

    return render(request, 'cursoLEI/criar_area.html')

@login_required
def editar_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    docentes = Docente.objects.all()
    areas = Area_Cientifica.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        ano = request.POST.get('ano')
        semestre = request.POST.get('semestre')
        ects = request.POST.get('ects')
        code = request.POST.get('code')
        conteudos = request.POST.get('conteudos')
        area_cientifica_id = request.POST.get('area')
        area_cientifica = Area_Cientifica.objects.get(id=area_cientifica_id)

        disciplina.nome = nome
        disciplina.ano = ano
        disciplina.semestre = semestre
        disciplina.ects = ects
        disciplina.code = code
        disciplina.conteudos = conteudos
        disciplina.area_cientifica = area_cientifica
        disciplina.save()

        docente_ids = request.POST.getlist('docentes')
        for docente in docentes:
            if str(docente.id) in docente_ids:
                if disciplina not in docente.disciplina.all():
                    docente.disciplina.add(disciplina)
            else:
                if disciplina in docente.disciplina.all():
                    docente.disciplina.remove(disciplina)

        return redirect('cursoLEI:lista_disciplina')

    return render(request, 'cursoLEI/editar_disciplina.html', {'disciplina': disciplina, 'areas': areas, 'docentes': docentes})


@login_required
def remover_disciplina_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina.delete()
    return redirect('cursoLEI:lista_disciplina')

@login_required
def criar_disciplina_view(request):
    areas = Area_Cientifica.objects.all()
    docentes = Docente.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        ano = request.POST.get('ano')
        semestre = request.POST.get('semestre')
        ects = request.POST.get('ects')
        code = request.POST.get('code')
        conteudos = request.POST.get('conteudos')
        area_cientifica_id = request.POST.get('area')
        area_cientifica = Area_Cientifica.objects.get(id=area_cientifica_id)

        disciplina = Disciplina(
            nome=nome, ano=ano, semestre=semestre,
            ects=ects, code=code, conteudos=conteudos,
            area_cientifica=area_cientifica
        )
        disciplina.save()

        docente_ids = request.POST.getlist('docentes')
        for docente in docentes:
            if str(docente.id) in docente_ids:
                if disciplina not in docente.disciplina.all():
                    docente.disciplina.add(disciplina)
            else:
                if disciplina in docente.disciplina.all():
                    docente.disciplina.remove(disciplina)

        return redirect('cursoLEI:lista_disciplina')

    return render(request, 'cursoLEI/criar_disciplina.html', {'areas': areas, 'docentes': docentes})


@login_required
def editar_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = Disciplina.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        apresentacao = request.POST.get('apresentacao')
        competencias = request.POST.get('competencias')
        objetivos = request.POST.get('objetivos')
        disciplinas_ids = request.POST.getlist('disciplinas')

        curso.nome = nome
        curso.apresentacao = apresentacao
        curso.competencias = competencias
        curso.objetivos = objetivos
        curso.save()

        if disciplinas_ids:
            disciplinas_selecionadas = Disciplina.objects.filter(id__in=disciplinas_ids)
            curso.disciplinas.set(disciplinas_selecionadas)

        curso.save()
        return redirect('cursoLEI:lista')
    return render(request, 'cursoLEI/editar_curso.html', {'curso': curso, 'disciplinas': disciplinas})

@login_required
def remover_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso.delete()
    return redirect('cursoLEI:lista')

@login_required
def criar_curso_view(request):
    disciplinas = Disciplina.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        objetivos = request.POST.get('objetivos')
        competencias = request.POST.get('competencias')
        apresentacao = request.POST.get('apresentacao')
        disciplinas_ids = request.POST.getlist('disciplinas')

        curso = Curso(nome=nome, competencias=competencias, apresentacao=apresentacao, objetivos=objetivos)
        curso.save()

        if disciplinas_ids:
            disciplinas_selecionadas = Disciplina.objects.filter(id__in=disciplinas_ids)
            curso.disciplinas.set(disciplinas_selecionadas)

        curso.save()
        return redirect('cursoLEI:lista')

    return render(request, 'cursoLEI/criar_curso.html', {'disciplinas': disciplinas})

def registo_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        raw_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if raw_password != confirm_password:
            return render(request, 'cursoLEI/registo.html', {'error_message': 'As senhas não coincidem'})

        user = User.objects.create_user(username=username, email=email, password=raw_password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        authenticated_user = authenticate(username=username, password=raw_password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('cursoLEI:lista')
        else:
            return render(request, 'cursoLEI/registo.html', {'error_message': 'Falha ao autenticar o usuário'})

    return render(request, 'cursoLEI/registo.html')

@login_required
def editar_perfil_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if new_password and confirm_password:
            if new_password == confirm_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
            else:
                messages.error(request, "As senhas não coincidem. A senha não foi alterada.")

        user.save()

        return redirect('cursoLEI:perfil')

    return render(request, 'cursoLEI/editar_perfil.html')

def perfil_view(request):
    return render(request, "cursoLEI/perfil.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('cursoLEI:lista')
    return render(request, "cursoLEI/perfil.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cursoLEI:lista')
        else:
            mensagem = "Credenciais inválidas. Tente novamente!"
            return render(request, 'cursoLEI/login.html', {'mensagem': mensagem})
    return render(request, 'cursoLEI/login.html')

def lista_view(request):
    cursos = Curso.objects.all()
    return render(request, 'cursoLEI/lista.html', {'cursos': cursos})

def lista_disciplina_view(request):
    disciplinas = Disciplina.objects.all()
    docentes = Docente.objects.all()
    return render(request, 'cursoLEI/lista_disciplina.html', {'disciplinas': disciplinas, 'docentes': docentes})

def curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplinas = curso.disciplinas.all()
    context = {'curso': curso, 'disciplinas': disciplinas}
    return render(request, 'cursoLEI/curso.html', context)

def disciplina_curso_view(request, curso_nome, disciplina_nome):
    curso = Curso.objects.get(nome=curso_nome)
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    docentes = Docente.objects.filter(disciplina=disciplina)
    context = {'disciplina': disciplina, 'projetos': projetos, 'curso': curso, 'docentes': docentes}
    return render(request, 'cursoLEI/disciplina.html', context)

def disciplina_view(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    projetos = Projeto.objects.filter(disciplina=disciplina)
    docentes = Docente.objects.filter(disciplina=disciplina)
    context = {'disciplina': disciplina, 'projetos': projetos, 'docentes': docentes}
    return render(request, 'cursoLEI/disciplina.html', context)

def docente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    return render(request, 'cursoLEI/docente.html', {'docente': docente})

def projeto_disciplina_view(request, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    context = {'projeto': projeto}
    return render(request, 'cursoLEI/projeto.html', context)

def projeto_view(request, projeto_nome, curso_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    curso = Curso.objects.get(nome=curso_nome)
    context = {'projeto': projeto, 'curso': curso}
    return render(request, 'cursoLEI/projeto.html', context)