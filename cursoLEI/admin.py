from django.contrib import admin

# Register your models here.
from cursoLEI.models import Curso
from cursoLEI.models import Area_Cientifica
from cursoLEI.models import Disciplina
from cursoLEI.models import Projeto
from cursoLEI.models import Linguagem_Programacao
from cursoLEI.models import Docente

admin.site.register(Area_Cientifica)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Linguagem_Programacao)
admin.site.register(Projeto)
admin.site.register(Docente)