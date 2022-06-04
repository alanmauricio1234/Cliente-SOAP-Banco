from django import forms
from datetime import date
import re
from django.core.exceptions import ValidationError

exp = '^[0-9][0-9][0-9][0-9]'

class TarjertaForm(forms.Form):
    n_tarjeta = forms.CharField(
        label='Numero de Tarjeta', 
        max_length=4, 
        required=True)
    n_tarjeta.widget.attrs.update({
        'class': 'controls',
        'placeholder': 'Ej. 1111'})
    
    def clean_n_tarjeta(self):
        # Validación de un número de tarjeta
        data = self.cleaned_data['n_tarjeta']
        if re.match(exp, data) is None:
            raise ValidationError('No cumple con el formato: ####')
        
        return data

class NipForm(forms.Form):
    nip = forms.CharField(
        label='Ingresa tu NIP',
        required=True,
        max_length=4,
        widget=forms.PasswordInput
    )
    nip.widget.attrs.update({
        'class': 'controls',
        'placeholder': '****'
    })

    def clean_nip(self):
        data = self.cleaned_data['nip']
        if re.match(exp, data) is None:
            raise ValidationError('El nip debe de tener 4 números. Ej. ****')
        return data

class PagoForm(forms.Form):
    pago = forms.FloatField(
            label='Ingresa la cantidad a retirar',
            min_value=0.0, 
            required=True)
    pago.widget.attrs.update({
        'class': 'controls',
        'placeholder': '$##.##'
    })

    def clean_pago(self):
        data = self.cleaned_data['pago']
        if data <= 0:
            raise ValidationError('El retiro debe ser mayor a cero')
        return data