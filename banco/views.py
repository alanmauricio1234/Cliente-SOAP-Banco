from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.urls import reverse
from .forms import NipForm, TarjertaForm
from .client import ClienteServicio

# Create your views here.
cliente = ClienteServicio()

class FormularioTarjeta(HttpRequest):
    def ingresar_tarjeta(request):
        form = TarjertaForm()
        mensaje = ''
        if request.method == 'POST':
            form = TarjertaForm(request.POST)
            if form.is_valid():
                n_tarjeta = form.cleaned_data['n_tarjeta']
                cliente.n_tarjeta = n_tarjeta
                mensaje = cliente.verifica_tarjeta()
                if not mensaje:
                    return redirect(reverse('banco:ingresar_nip'))
        return render(request, 
                        "formularios/ingresar.html",
                        {'form' : form,
                        'mensaje': mensaje})

class FormularioNip(HttpRequest):
    def ingresa_nip(request):
        form = NipForm()
        mensaje = ''
        intentos = cliente.consultar_intentos()
        print(request)
        if request.method == 'POST':
            form = NipForm(request.POST)
            if form.is_valid():
                nip = int(form.cleaned_data['nip'])
                mensaje = cliente.verificar_nip(nip)
                if not mensaje:
                    print('Todo salio chido :)')
        
        return render(request, 
                'formularios/ingresar_nip.html',
                {'form': form,
                'mensaje': mensaje,
                'intentos': intentos})
            

    
        