from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'cursoLEI'

urlpatterns = [
    path('perfil/', views.logout_view, name='logout'),
    path('lista/', views.lista_view, name='lista'),
    path('lista_disciplina/', views.lista_disciplina_view, name='lista_disciplina'),
    path('curso/<str:curso_nome>/', views.curso_view, name='curso'),
    path('projeto/<str:curso_nome>/<str:projeto_nome>/', views.projeto_view, name='projeto'),
    path('projeto/<str:projeto_nome>/', views.projeto_disciplina_view, name='projeto_disciplina'),
    path('disciplina/<str:curso_nome>/<str:disciplina_nome>/', views.disciplina_curso_view, name='disciplina'),
    path('disciplina/<str:disciplina_nome>/', views.disciplina_view, name='disciplina_lista'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.logout_view, name='perfil'),
    path('editar_perfil/', views.editar_perfil_view, name='editar_perfil'),
    path('registo/', views.registo_view, name='registo'),
    path('lista/<int:curso_id>/', views.remover_curso_view, name='remover_curso'),
    path('criar_curso/', views.criar_curso_view, name='criar_curso'),
    path('editar_curso/<str:curso_id>/', views.editar_curso_view, name='editar_curso'),
    path('criar_disciplina/', views.criar_disciplina_view, name='criar_disciplina'),
    path('editar_disciplina/<str:disciplina_id>/', views.editar_disciplina_view, name='editar_disciplina'),
    path('lista_disciplina/<int:disciplina_id>/', views.remover_disciplina_view, name='remover_disciplina'),
    path('criar_area/<str:disciplina_id>/', views.criar_area_editar_view, name='criar_area_editar'),
    path('criar_area/', views.criar_area_criar_view, name='criar_area_criar'),
    path('remover_area/', views.remover_area_pagina_view, name='remover_area_pagina'),
    path('remover_area/<int:area_id>/', views.remover_area_view, name='remover_area'),
    path('criar_projeto/<str:disciplina_id>/', views.criar_projeto_view, name='criar_projeto'),
    path('editar_projeto/<str:projeto_id>/', views.editar_projeto_view, name='editar_projeto'),
    path('remover_projeto/<int:projeto_id>/', views.remover_projeto_view, name='remover_projeto'),
    path('criar_lingua/<str:projeto_id>/', views.criar_lingua_view, name='criar_lingua'),
    path('remover_lingua/<str:projeto_id>/', views.remover_lingua_view, name='remover_lingua'),
    path('criar_docente/', views.criar_docente_view, name='criar_docente'),
    path('remover_docente/<str:docente_id>/', views.remover_docente_view, name='remover_docente'),
    path('lista_docente/', views.lista_docente_view, name='lista_docente'),
    path('docente/<str:docente_id>/', views.docente_view, name='docente'),
]