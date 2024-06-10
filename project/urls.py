from django.contrib import admin
from django.urls import path, include   # incluir include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),  # novo path
    path('pwsite/', include('pwsite.urls')),
    path('bandas/', include('bandas.urls')),
    path('Artigos/', include('Artigos.urls')),
    path('cursoLEI/', include('cursoLEI.urls')),
    path('meteo/', include('meteo.urls')),
    path('praias/', include('praias.urls')),
    path('', include('portfolio.urls')),
]