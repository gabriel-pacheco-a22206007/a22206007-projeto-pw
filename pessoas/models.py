from django.db import models

# Create your models here.
class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length = 200)
    segundo_nome = models.CharField(max_length = 200)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.primeiro_nome} {self.segundo_nome} tem {self.idade} anos"