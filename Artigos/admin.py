from django.contrib import admin
from .models import Artigo
from .models import Autor
from .models import Rating
from .models import Comentario

# Register your models here.
admin.site.register(Artigo)
admin.site.register(Autor)
admin.site.register(Rating)
admin.site.register(Comentario)