from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, 'portfolio/index.html')

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

        return redirect('portfolio:perfil')

    return render(request, 'portfolio/perfil_editar.html')

def perfil_view(request):
    return render(request, "portfolio/perfil.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('portfolio:index')
    return render(request, "portfolio/perfil.html")

def registo_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        raw_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if raw_password != confirm_password:
            return render(request, 'portfolio/registo.html', {'error_message': 'As senhas não coincidem'})

        user = User.objects.create_user(username=username, email=email, password=raw_password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        authenticated_user = authenticate(username=username, password=raw_password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('portfolio:index')
        else:
            return render(request, 'portfolio/registo.html', {'error_message': 'Falha ao autenticar o usuário'})

    return render(request, 'portfolio/registo.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio:index')
        else:
            mensagem = "Credenciais inválidas. Tente novamente!"
            return render(request, 'portfolio/login.html', {'mensagem': mensagem})
    return render(request, 'portfolio/login.html')