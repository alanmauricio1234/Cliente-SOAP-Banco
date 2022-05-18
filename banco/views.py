from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.urls import reverse
from .forms import NipForm, TarjertaForm, PagoForm
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
                mensaje = cliente.verifica_tarjeta(n_tarjeta)
                if not mensaje:
                    if not cliente.verificar_tarjeta_bloqueada(n_tarjeta):
                        return redirect(reverse('banco:ingresar_nip', args=[n_tarjeta]), 
                                        kwargs={'n_tarjeta' : n_tarjeta})
                    else:
                        mensaje = 'Lo sentimos tu tarjeta esta bloqueada :('
        return render(request, 
                        "formularios/ingresar.html",
                        {'form' : form,
                        'mensaje': mensaje})

class FormularioNip(HttpRequest):
    def ingresa_nip(request, n_tarjeta):
        mensaje = cliente.verifica_tarjeta(n_tarjeta)
        if not mensaje:
            if request.method == 'GET':
                form = NipForm()
            if request.method == 'POST':
                form = NipForm(request.POST)
                if form.is_valid():
                    nip = int(form.cleaned_data['nip'])
                    mensaje = cliente.verificar_nip(n_tarjeta,nip)
                    if not mensaje:
                        return redirect(reverse('banco:retirar', args=[n_tarjeta]),
                                        kwargs={'n_tarjeta': n_tarjeta})
            intentos = cliente.consultar_intentos(n_tarjeta)
            # Si la tarjeta esta bloqueada
            if cliente.verificar_tarjeta_bloqueada(n_tarjeta):
                mensaje = 'Lo sentimos tu tarjeta esta bloqueada :('
                form.fields['nip'].disabled = True
            
            return render(request, 
                    'formularios/ingresar_nip.html',
                    {'form': form,
                    'mensaje': mensaje,
                    'intentos': intentos})
        
        return redirect(reverse('banco:ingresar_n_tarjeta'))

class FormularioPago(HttpRequest):
    def retirar(request, n_tarjeta):
        if cliente.verificar_tarjeta_completa(n_tarjeta):
            mensaje = ''
            saldo = cliente.consulta_saldo(n_tarjeta)
            limite = cliente.consulta_limite(n_tarjeta)
            if request.method == 'GET':
                form = PagoForm()
            if request.method == 'POST':
                form = PagoForm(request.POST)
                if form.is_valid():
                    pago = form.cleaned_data['pago']
                    if pago <= limite:
                        if pago <= saldo:
                            pago = cliente.realiza_pago(n_tarjeta, pago)
                            saldo = pago #Asiganmos el nuevo saldo
                        else:
                            mensaje = 'No tienes suficientes fondos :('
                    else:
                        mensaje = 'No puedes rebasar el limite de retiro :('

            return render(request,
                        'formularios/cliente.html',
                        {'form': form,
                        'mensaje': mensaje,
                        'saldo': saldo,
                        'limite': limite})

        return redirect(reverse('banco:ingresar_n_tarjeta'))

        

    
    

    
        