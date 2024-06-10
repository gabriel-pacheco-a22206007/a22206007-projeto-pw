from django.shortcuts import render
from praias.models import Praia, Servico, Regiao

# Create your views here.
def praias_view(request):
    regioes = Regiao.objects.all()
    regiao_praias = []

    for regiao in regioes:
        praia = Praia.objects.filter(regiao = regiao)
        regiao_praias.append((regiao.nome, praia))

    return render(request, 'praias/praias.html', {'regiao_praias': regiao_praias})

def praia_view(request, praia_nome):
    praia = Praia.objects.get(nome = praia_nome)
    return render(request, 'praias/praia.html', {'praia': praia})