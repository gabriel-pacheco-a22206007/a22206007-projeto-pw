from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from Artigos.models import Autor
from Artigos.models import Artigo
from Artigos.models import Comentario
from Artigos.models import Rating
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required
def autor_editar_view(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        autor.nome = nome
        autor.email = email
        autor.bio = bio
        autor.save()

        return redirect('Artigos:lista_autor')
    return render(request, 'artigos/autor_editar.html', {'autor': autor})

@login_required
def comentario_editar_view(request, comentario_id):
    autores = Autor.objects.all()
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    context = {'comentario': comentario, 'autores': autores}
    if request.method == 'POST':
        comentario_v = request.POST.get('comentario')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)

        comentario.comentario = comentario_v
        comentario.autor_id = autor
        comentario.save()


        artigo = comentario.artigo_id
        return redirect('Artigos:artigos_detalhes', artigo.artigo_id)
    return render(request, 'artigos/comentario_editar.html', context)

@login_required
def rating_editar_view(request, rating_id):
    autores = Autor.objects.all()
    rating = get_object_or_404(Rating, pk=rating_id)
    context = {'rating': rating, 'autores': autores}
    if request.method == 'POST':
        rating_v = request.POST.get('rating')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)

        rating.rating = rating_v
        rating.autor_id = autor
        rating.save()


        artigo = rating.artigo_id
        return redirect('Artigos:artigos_detalhes', artigo.artigo_id)
    return render(request, 'artigos/rating_editar.html', context)

@login_required
def artigo_editar_view(request, artigo_id):
    autores = Autor.objects.all()
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    context = {'artigo': artigo, 'autores': autores}
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)

        artigo.titulo = titulo
        artigo.conteudo = conteudo
        artigo.autor_id = autor
        artigo.save()

        return redirect('Artigos:lista')
    return render(request, 'artigos/artigo_editar.html', context)

@login_required
def rating_remover_view(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    artigo_id = rating.artigo_id.artigo_id
    rating.delete()
    return redirect('Artigos:artigos_detalhes', artigo_id=artigo_id)

@login_required
def criar_rating_view(request, artigo_id):
    artigo = Artigo.objects.get(artigo_id=artigo_id)
    autores = Autor.objects.all()
    context = {'artigo': artigo, 'autores': autores}

    if request.method == 'POST':
        rating_txt = request.POST.get('rating')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)
        rating = Rating(autor_id=autor, rating=rating_txt, artigo_id=artigo)
        rating.save()
        return redirect('Artigos:artigos_detalhes', artigo_id=artigo_id)

    return render(request, 'artigos/criar_rating.html', context)

@login_required
def comentario_remover_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    artigo_id = comentario.artigo_id.artigo_id
    comentario.delete()
    return redirect('Artigos:artigos_detalhes', artigo_id=artigo_id)

@login_required
def criar_comentario_view(request, artigo_id):
    artigo = Artigo.objects.get(artigo_id=artigo_id)
    autores = Autor.objects.all()
    context = {'artigo': artigo, 'autores': autores}

    if request.method == 'POST':
        comentario_txt = request.POST.get('comentario')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)
        comentario = Comentario(autor_id=autor, comentario=comentario_txt, artigo_id=artigo)
        comentario.save()
        return redirect('Artigos:artigos_detalhes', artigo_id=artigo_id)

    return render(request, 'artigos/criar_comentario.html', context)

@login_required
def autor_remover_view(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    autor.delete()
    return redirect('Artigos:lista_autor')

@login_required
def criar_autor_view(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        autor = Autor(nome=nome, email=email, bio=bio)
        autor.save()
        return redirect('Artigos:lista_autor')

    return render(request, 'artigos/criar_autor.html')

@login_required
def criar_artigo_view(request):
    autores = Autor.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        autor_id = request.POST.get('autor')

        autor = Autor.objects.get(autor_id=autor_id)
        artigo = Artigo(titulo=titulo, conteudo=conteudo, autor_id=autor)
        artigo.save()
        return redirect('Artigos:lista')

    return render(request, 'artigos/criar_artigo.html', {'autores': autores})

@login_required
def artigo_remover_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    artigo.delete()
    return redirect('Artigos:lista')

@login_required
def perfil_editar_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = request.user

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, 'Perfil atualizado com sucesso.')

        return redirect('Artigos:perfil')

    return render(request, 'artigos/perfil_editar.html')

def perfil_view(request):
    return render(request, "artigos/perfil.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('Artigos:lista')
    return render(request, "artigos/perfil.html")

def registo_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        raw_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if raw_password != confirm_password:
            return render(request, 'artigos/registo.html', {'error_message': 'As senhas não coincidem'})

        user = User.objects.create_user(username=username, email=email, password=raw_password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        authenticated_user = authenticate(username=username, password=raw_password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('Artigos:lista')
        else:
            return render(request, 'artigos/registo.html', {'error_message': 'Falha ao autenticar o usuário'})

    return render(request, 'artigos/registo.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Artigos:lista')
        else:
            mensagem = "Credenciais inválidas. Tente novamente!"
            return render(request, 'artigos/login.html', {'mensagem': mensagem})
    return render(request, 'artigos/login.html')

def lista_view(request):
    artigos = Artigo.objects.all()
    return render(request, "artigos/lista.html", {'artigos':artigos})

def lista_autor_view(request):
    autores = Autor.objects.all()
    return render(request, "artigos/lista_autor.html", {'autores':autores})

def autor_view(request, autor_id):
    autor = Autor.objects.get(autor_id=autor_id)
    artigos = Artigo.objects.filter(autor_id = autor)
    context = {'autor':autor, 'artigos': artigos}
    return render(request, "artigos/autor.html", context)

def artigo_detalhes_view(request, artigo_id):
    artigo = Artigo.objects.get(artigo_id=artigo_id)
    comentarios = Comentario.objects.filter(artigo_id = artigo)
    ratings = Rating.objects.filter(artigo_id = artigo)
    autor = artigo.autor_id
    context = {'artigo': artigo, 'comentarios': comentarios, 'ratings': ratings, 'autor': autor}
    return render(request, "artigos/artigos_detalhes.html", context)