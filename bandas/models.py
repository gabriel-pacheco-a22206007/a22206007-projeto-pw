from django.db import models

# Create your models here.
class Banda(models.Model):
    nome = models.CharField(max_length = 100)
    ano_criacao = models.IntegerField()
    nacionalidade = models.CharField(max_length = 100, default = '---')
    foto = models.ImageField()

    def __str__(self):
        return f"{self.nome} foi criada no ano de {self.ano_criacao}"

class Album(models.Model):
    titulo = models.CharField(max_length = 100)
    ano_lancamento = models.IntegerField()
    capa = models.ImageField()
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'banda_album')

    def __str__(self):
        return f"{self.titulo} foi lancado no ano de {self.ano_lancamento}"

class Musica(models.Model):
    titulo = models.CharField(max_length = 100)
    ano_lancamento = models.IntegerField()
    link = models.URLField(max_length = 200)
    duracao = models.CharField(max_length = 100, default = '00:00')
    letra = models.TextField(default = 'letra não disponível')
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = 'album_musica')

    def __str__(self):
        return f"{self.titulo} foi lancado no ano de {self.ano_lancamento}"
