# Generated by Django 4.0.6 on 2024-04-21 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Cientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apresentacao', models.TextField()),
                ('objetivos', models.TextField()),
                ('competencias', models.TextField()),
                ('nome', models.CharField(default='Curso sem nome', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=20)),
                ('ects', models.IntegerField()),
                ('curricularIUnitReadableCode', models.CharField(max_length=50)),
                ('area_cientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_area', to='cursoLEI.area_cientifica')),
            ],
        ),
        migrations.CreateModel(
            name='Linguagem_Programacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('conceitos_aplicados', models.TextField()),
                ('tecnologias_usadas', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projeto_imagens/')),
                ('link_video_youtube', models.URLField(blank=True, default='https://www.youtube.com/')),
                ('link_github', models.URLField(blank=True, default='https://github.com/')),
                ('disciplina', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cursoLEI.disciplina')),
                ('linguagem_programacao', models.ManyToManyField(to='cursoLEI.linguagem_programacao')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disciplinas', models.ManyToManyField(to='cursoLEI.disciplina')),
            ],
        ),
    ]
