from django.urls import path
from . import views

app_name = 'banco'

urlpatterns = [
    path('ingresar/', views.FormularioTarjeta.ingresar_tarjeta, name='ingresar_n_tarjeta'),
    path('ingresar/nip/<str:n_tarjeta>/', views.FormularioNip.ingresa_nip, name='ingresar_nip'),
    path('cliente/<str:n_tarjeta>/', views.FormularioPago.retirar, name='retirar')
]
