from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from secador.models import Secador


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        modelo = request.POST['modelo']
        localizacao = request.POST['localizacao']

        user = get_object_or_404(User, pk=request.user.id)

        secador = Secador.objects.create(usuario=user, nome=nome, modelo=modelo, localizacao=localizacao)
        secador.save()
        return redirect('home')

    return render(request, 'secador/cadastro.html')


def buscar(request):

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            print(nome_a_buscar)

            secador = Secador.objects.filter(nome__icontains=nome_a_buscar)

            dados = {
                'secadores': secador
            }
            return render(request, 'secador/buscar.html', dados)

    return render(request, 'secador/buscar.html')


def detail(request, secador_id):
    secador = get_object_or_404(Secador, pk=secador_id)

    dados = {
        'secador': secador
    }
    return render(request, 'secador/detail.html', dados)


def excluir(request, secador_id):
    Secador.objects.filter(id=secador_id).delete()

    return redirect('home')

