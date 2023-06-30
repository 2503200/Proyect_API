from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from veterinarios.models import Veterinario


# Create your views here.
def ver_veterinarios(request):
    canti_veteri = Veterinario.objects.count()
    pagina = loader.get_template('veterinarios.html')
    lista_veteri = Veterinario.objects.order_by('apellido','nombre')
    datos = {'cantidad': canti_veteri, 'veterinarios': lista_veteri}
    return HttpResponse(pagina.render(datos, request))