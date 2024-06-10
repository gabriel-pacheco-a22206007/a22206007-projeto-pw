# Generated by Django 4.0.6 on 2024-04-21 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursoLEI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='curricularIUnitReadableCode',
        ),
        migrations.RemoveField(
            model_name='docente',
            name='disciplinas',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='conceitos_aplicados',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='linguagem_programacao',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='link_github',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='link_video_youtube',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='tecnologias_usadas',
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(related_name='cursos', to='cursoLEI.disciplina', verbose_name='Disciplinas'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='code',
            field=models.IntegerField(default='0', verbose_name='curricularIUnitReadableCode'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='conteudos',
            field=models.CharField(default='Conteúdos Programáticos Padrão', max_length=500, verbose_name='Conteúdos Programáticos'),
        ),
        migrations.AddField(
            model_name='docente',
            name='disciplina',
            field=models.ManyToManyField(to='cursoLEI.disciplina', verbose_name='Disciplina/s'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='conceitos',
            field=models.TextField(default='0', verbose_name='Conceitos Aplicados'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='foto',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagem do Projeto'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='gitLink',
            field=models.URLField(null=True, verbose_name='Link Repositório GitHub'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='linguagens',
            field=models.ManyToManyField(to='cursoLEI.linguagem_programacao', verbose_name='Linguagens de Programação'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='nome',
            field=models.CharField(default='Nome', max_length=100, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tecnologias',
            field=models.TextField(default='0', verbose_name='Tecnologias Usadas'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='video',
            field=models.URLField(null=True, verbose_name='Link Video do Youtube'),
        ),
        migrations.AlterField(
            model_name='area_cientifica',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='apresentacao',
            field=models.TextField(verbose_name='Apresentação'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='competencias',
            field=models.TextField(verbose_name='Competências'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='objetivos',
            field=models.TextField(verbose_name='Objetivos'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='ano',
            field=models.IntegerField(verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='area_cientifica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoLEI.area_cientifica'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='ects',
            field=models.IntegerField(verbose_name='Ects'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='semestre',
            field=models.IntegerField(verbose_name='Semestre'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='linguagem_programacao',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoLEI.disciplina'),
        ),
    ]
