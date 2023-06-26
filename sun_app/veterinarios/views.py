from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from veterinarios.forms import VeterinarioFormulario
from veterinarios.models import Veterinario

#VeterinarioFormulario = modelform_factory(Veterinario, exclude=[])
# Create your views here.
def agregar_veteri(request):
    pagina = loader.get_template('agregar_veteri.html')
    if request.method == 'GET':
        formulario = VeterinarioFormulario
    elif request.method == 'POST':
        formulario = VeterinarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

