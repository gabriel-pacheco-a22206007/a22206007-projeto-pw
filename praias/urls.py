from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'praias'

urlpatterns = [
    path('praias/', views.praias_view, name='praias'),
    path('praia/<str:praia_nome>/', views.praia_view, name='praia'),
]