from django.db import models

# Create your models here.
class Regiao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self):
        return f'Nome: {self.nome}'

class Servico(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self):
        return f'Nome: {self.nome}'

class Praia(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    regiao = models.ForeignKey('Regiao', on_delete=models.CASCADE)
    servicos = models.ManyToManyField('Servico', related_name='praias', verbose_name='Servicos')
    foto = models.ImageField(null=True)

    def __str__(self):
        return f'Nome: {self.nome}'