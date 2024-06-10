from django.db import models

# Create your models here.
class Autor(models.Model):
    autor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    artigo_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    visivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} realizado por {self.autor_id}"

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    comentario = models.TextField()
    artigo_id = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comentario} realizado por {self.autor_id} ao artigo {self.artigo_id}"

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    artigo_id = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    data_rating = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artigo_id}, foi dado o rating de {self.rating} pelo {self.autor_id}"
