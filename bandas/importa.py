import json
from bandas.models import Banda
from bandas.models import Album
from bandas.models import Musica

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open('bandas/json/bandasGPT.json') as f:
    bandas = json.load(f)

    for banda in bandas:

        Banda.objects.create(
             nome = banda.get('nome'),
             ano_criacao = banda.get('ano_criacao'),
             nacionalidade = banda.get('nacionalidade')
        )

with open('bandas/json/discosGPT.json') as f:
    albuns = json.load(f)

    for album_info in albuns:

        album_created = Album.objects.create(
             titulo = album_info.get('titulo'),
             ano_lancamento = album_info.get('ano_lancamento'),
             banda = Banda.objects.get(nome = album_info.get('banda'))
        )

        for musica in album_info['musicas']:
                 Musica.objects.create(
                     titulo = musica.get('titulo'),
                     duracao = musica.get('duracao'),
                     album = album_created,
                     ano_lancamento = album_created.ano_lancamento
                     )