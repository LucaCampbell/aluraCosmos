from django.shortcuts import render, get_object_or_404

from .models import Fotografia


def index(request):
    fotos = Fotografia.objects.filter(publicada=True)

    dados = {
        'fotos': fotos
    }

    return render(request, 'galeria/index.html', dados)


def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)

    foto_a_exibir = {
        'foto': foto
    }

    return render(request, 'galeria/imagem.html', foto_a_exibir)
