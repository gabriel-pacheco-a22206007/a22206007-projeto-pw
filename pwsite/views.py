from django.shortcuts import render

def index_view(request):
    return render(request, "pwsite/index.html")

def sobre_view(request):
    return render(request, "pwsite/sobre.html")

def pagina_view(request):
    return render(request, "pwsite/pagina.html")