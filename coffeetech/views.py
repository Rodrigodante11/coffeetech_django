from django.shortcuts import render
from secador.models import Secador


def home(request):
    if request.user.is_authenticated:
        secador = Secador.objects.filter(usuario=request.user.id)

        dados = {
            'secadores': secador
        }
        return render(request, 'coffeetech/home.html',  dados)

    return render(request, 'coffeetech/home.html')




