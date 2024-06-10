from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('layout/', views.layout_view, name='layout'),
    path('perfil/', views.logout_view, name='logout'),
    path('1-lista/<int:banda_id>/remover/', views.banda_remover_view, name='banda_remover'),
    path('2-banda_albuns/<int:album_id>/remover/', views.album_remover_view, name='album_remover'),
    path('3-album/<int:musica_id>/remover/', views.musica_remover_view, name='musica_remover'),
    path('1-lista/', views.lista_view, name='1-lista'),
    path('2-banda_albuns/<str:banda_nome>/', views.banda_albuns_view, name='2-banda_albuns'),
    path('3-album/<str:album_titulo>/', views.album_view, name='3-album'),
    path('4-musica/<str:musica_titulo>/', views.musica_view, name='4-musica'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('registo/', views.registo_view, name='registo'),
    path('add_banda/', views.banda_add_view, name='add_banda'),
    path('perfil_editar/', views.perfil_editar_view, name='perfil_editar'),
    path('add_album/<str:banda_nome>/', views.album_add_view, name='add_album'),
    path('add_musica/<str:album_titulo>/', views.musica_add_view, name='add_musica'),
    path('banda_editar/<str:banda_id>/', views.banda_editar_view, name='banda_editar'),
    path('album_editar/<str:album_id>/', views.album_editar_view, name='album_editar'),
    path('musica_editar/<str:musica_id>/', views.musica_editar_view, name='musica_editar'),
]