from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def nome_view(request):
    return HttpResponse("O meu nome é Gabriel Pacheco!")
    
def dt_nascimento_view(request):
    return HttpResponse("Nasci no dia 18/09/2003!")
    
def num_aluno_view(request):
    return HttpResponse("O meu número de aluno é a22206007!")