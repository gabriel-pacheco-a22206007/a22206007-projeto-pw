from django.contrib import admin

# Register your models here.
from praias.models import Praia
from praias.models import Servico
from praias.models import Regiao

admin.site.register(Praia)
admin.site.register(Servico)
admin.site.register(Regiao)