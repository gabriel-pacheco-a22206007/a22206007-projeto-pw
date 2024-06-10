from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view),
    path('nome/', views.nome_view),
    path('dt_nascimento/', views.dt_nascimento_view),
    path('num_aluno/', views.num_aluno_view),
]