from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'Artigos'

urlpatterns = [
    path('artigos_detalhes/<str:rating_id>/remover_rating/', views.rating_remover_view, name='rating_remover'),
    path('lista/<str:artigo_id>/remover/', views.artigo_remover_view, name='artigo_remover'),
    path('lista_autor/<str:autor_id>/remover/', views.autor_remover_view, name='autor_remover'),
    path('artigos_detalhes/<str:comentario_id>/remover_comentario/', views.comentario_remover_view, name='comentario_remover'),
    path('lista/', views.lista_view, name='lista'),
    path('criar_artigo/', views.criar_artigo_view, name='criar_artigo'),
    path('criar_autor/', views.criar_autor_view, name='criar_autor'),
    path('criar_comentario/<str:artigo_id>/', views.criar_comentario_view, name='criar_comentario'),
    path('criar_rating/<str:artigo_id>/', views.criar_rating_view, name='criar_rating'),
    path('autor/<str:autor_id>', views.autor_view, name='autor'),
    path('artigos_detalhes/<str:artigo_id>/', views.artigo_detalhes_view, name='artigos_detalhes'),
    path('login/', views.login_view, name='login'),
    path('registo/', views.registo_view, name='registo'),
    path('perfil/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('lista_autor/', views.lista_autor_view, name='lista_autor'),
    path('perfil_editar/', views.perfil_editar_view, name='perfil_editar'),
    path('artigo_editar/<str:artigo_id>/', views.artigo_editar_view, name='artigo_editar'),
    path('rating_editar/<str:rating_id>/', views.rating_editar_view, name='rating_editar'),
    path('comentario_editar/<str:comentario_id>/', views.comentario_editar_view, name='comentario_editar'),
    path('autor_editar/<str:autor_id>/', views.autor_editar_view, name='autor_editar'),
]