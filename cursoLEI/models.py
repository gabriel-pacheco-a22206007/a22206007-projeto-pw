from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    disciplinas = models.ManyToManyField('Disciplina')

    def __str__(self):
        return f'Nome: {self.nome}'

class Area_Cientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'Área Ciêntifica: {self.nome}'

class Linguagem_Programacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'Nome: {self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    code = models.IntegerField()
    conteudos = models.CharField(max_length=500, default='Conteúdos Programáticos Padrão')
    area_cientifica = models.ForeignKey('Area_Cientifica', on_delete=models.CASCADE)

    def __str__(self):
        return f'Nome: {self.nome}'

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos = models.TextField()
    tecnologias = models.TextField()
    foto = models.ImageField(null=True)
    video = models.URLField(null=True)
    gitLink = models.URLField(null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    linguagens = models.ManyToManyField(Linguagem_Programacao)

    def __str__(self):
        return f'Nome: {self.nome}'

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.ManyToManyField(Disciplina)

    def __str__(self):
        return f'Nome: {self.nome}'
