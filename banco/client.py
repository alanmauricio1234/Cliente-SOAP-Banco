from zeep import Client

class ClienteServicio():
    client = Client('http://localhost:8000/soap_banco/?wsdl')
    n_tarjeta = ''
    def verifica_tarjeta(self):
        mensaje = ''
        if not (self.client.service.consulta_tarjeta(self.n_tarjeta)):
            mensaje = 'El número de tarjeta no está registado :('
        elif not (self.client.service.verifica_tarjeta(self.n_tarjeta)):
            mensaje = 'La tarjeta no está verificada'
        elif not (self.client.service.consulta_fecha(self.n_tarjeta)):
            mensaje = 'La fecha de vencimiento expiró'

        return mensaje

    def verificar_nip(self,nip):
        mensaje = ''
        if not (self.client.service.consulta_nip(self.n_tarjeta, nip)):
            mensaje = 'El NIP es incorrecto :('
        return mensaje

    def consultar_intentos(self):
        return self.client.service.consulta_intentos(self.n_tarjeta)

    def consulta_saldo(self):
        return self.client.service.consulta_saldo(self.n_tarjeta)
    
    def consulta_limite(self):
        return self.client.service.verifica_limite(self.n_tarjeta)

    def realiza_pago(self, pago):
        return self.client.service.realiza_pago(self.n_tarjeta, pago)
        