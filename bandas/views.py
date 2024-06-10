from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from bandas.models import Banda
from bandas.models import Album
from bandas.models import Musica
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def musica_add_view(request, album_titulo):
    album = Album.objects.get(titulo=album_titulo)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        ano_lancamento = request.POST.get('ano_lancamento')
        link = request.POST.get('link')
        duracao = request.POST.get('duracao')

        musica = Musica(titulo=titulo, ano_lancamento=ano_lancamento, link=link, duracao=duracao, album=album)
        musica.save()
        return redirect('bandas:3-album', album_titulo = album.titulo)
    return render(request, 'bandas/add_musica.html', {'album' : album})

@login_required
def musica_editar_view(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        ano_lancamento = request.POST.get('ano_lancamento')
        link = request.POST.get('link')
        duracao = request.POST.get('duracao')
        letra = request.POST.get('letra')

        musica.titulo = titulo
        musica.ano_lancamento = ano_lancamento
        musica.link = link
        musica.duracao = duracao
        musica.letra = letra

        musica.save()
        return redirect('bandas:3-album', album_titulo = musica.album.titulo)
    return render(request, 'bandas/musica_editar.html', {'musica': musica})

@login_required
def musica_remover_view(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    album = musica.album
    musica.delete()
    return redirect('bandas:3-album', album_titulo = album.titulo)

@login_required
def album_add_view(request, banda_nome):
    banda = Banda.objects.get(nome=banda_nome)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        ano_lancamento = request.POST.get('ano_lancamento')
        capa = request.POST.get('capa')

        album = Album(titulo=titulo, ano_lancamento=ano_lancamento, capa=capa, banda=banda)
        album.save()
        return redirect('bandas:2-banda_albuns', banda_nome = banda.nome)
    return render(request, 'bandas/add_album.html', {'banda' : banda})

@login_required
def album_editar_view(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        ano_lancamento = request.POST.get('ano_lancamento')

        album.titulo = titulo
        album.ano_lancamento = ano_lancamento
        album.save()
        return redirect('bandas:2-banda_albuns', banda_nome = album.banda.nome)
    return render(request, 'bandas/album_editar.html', {'album': album})

@login_required
def album_remover_view(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    banda = album.banda
    album.delete()
    return redirect('bandas:2-banda_albuns', banda_nome = banda.nome)

@login_required
def banda_add_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ano_criacao = request.POST.get('ano')
        nacionalidade = request.POST.get('nacionalidade')
        foto = request.POST.get('foto')

        banda = Banda(nome=nome, ano_criacao=ano_criacao, nacionalidade=nacionalidade, foto=foto)
        banda.save()
        return redirect('bandas:1-lista')
    return render(request, 'bandas/add_banda.html')

@login_required
def banda_editar_view(request, banda_id):
    banda_id = banda_id.replace('-', ' ').title()
    banda = Banda.objects.get(nome=banda_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ano_criacao = request.POST.get('ano')
        nacionalidade = request.POST.get('nacionalidade')
        foto = request.POST.get('foto')

        banda.nome = nome
        banda.ano_criacao = ano_criacao
        banda.nacionalidade = nacionalidade
        banda.foto = foto
        banda.save()
        return redirect('bandas:1-lista')
    return render(request, 'bandas/banda_editar.html', {'banda': banda})

@login_required
def banda_remover_view(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)
    banda.delete()
    return redirect('bandas:1-lista')

@login_required
def perfil_editar_view(request):
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

        messages.success(request, 'Perfil atualizado com sucesso.')

        return redirect('bandas:perfil')

    return render(request, 'bandas/perfil_editar.html')


def registo_view(request):
    if request.method == 'POST':
        username = request.POST.get('new_username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        raw_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if raw_password != confirm_password:
            return render(request, 'bandas/registo.html', {'error_message': 'As senhas não coincidem'})

        user = User.objects.create_user(username=username, email=email, password=raw_password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        authenticated_user = authenticate(username=username, password=raw_password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('bandas:layout')
        else:
            return render(request, 'bandas/registo.html', {'error_message': 'Falha ao autenticar o usuário'})

    return render(request, 'bandas/registo.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bandas:layout')
        else:
            mensagem = "Credenciais inválidas. Tente novamente!"
            return render(request, 'bandas/login.html', {'mensagem': mensagem})
    return render(request, 'bandas/login.html')

def layout_view(request):
    return render(request, "bandas/layout.html")

def perfil_view(request):
    return render(request, "bandas/perfil.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('bandas:layout')
    return render(request, "bandas/perfil.html")

def lista_view(request):
    bandas = Banda.objects.all()
    return render(request, "bandas/1-lista.html", {'bandas':bandas})

def banda_albuns_view(request, banda_nome):
    banda_nome = banda_nome.replace('-', ' ').title()
    banda = Banda.objects.get(nome=banda_nome)
    albuns = Album.objects.filter(banda=banda)
    context = {'banda': banda, 'albuns': albuns}
    return render(request, "bandas/2-banda_albuns.html", context)

def album_view(request, album_titulo):
    album = Album.objects.get(titulo=album_titulo)
    musicas = Musica.objects.filter(album=album)
    context = {'album': album, 'musicas': musicas}
    return render(request, "bandas/3-album.html", context)

def musica_view(request, musica_titulo):
    musica = Musica.objects.get(titulo=musica_titulo)
    return render(request, "bandas/4-musica.html", {'musica':musica})