from zeep import Client

class ClienteServicio():
    client = Client('http://localhost:8000/soap_banco/?wsdl')
    def verifica_tarjeta(self, n_tarjeta):
        mensaje = ''
        if not (self.client.service.consulta_tarjeta(n_tarjeta)):
            mensaje = 'El número de tarjeta no esta registado :('
        elif not (self.client.service.verifica_tarjeta(n_tarjeta)):
            mensaje = 'La tarjeta no esta verificada :('
        elif not (self.client.service.consulta_fecha(n_tarjeta)):
            mensaje = 'La fecha de vencimiento expiro :('

        return mensaje

    def verificar_tarjeta_completa(self, n_tarjeta):
        if not self.client.service.consulta_tarjeta(n_tarjeta):
            return False
        if not self.client.service.verifica_tarjeta(n_tarjeta):
            return False
        if not self.client.service.consulta_fecha(n_tarjeta):
            return False
        if self.client.service.verifica_tarjeta_bloqueada(n_tarjeta):
            return False
        return True

    def verificar_nip(self, n_tarjeta, nip):
        mensaje = ''
        if not (self.client.service.consulta_nip(n_tarjeta, nip)):
            mensaje = 'El NIP es incorrecto :('
        return mensaje

    def verificar_tarjeta_bloqueada(self, n_tarjeta):
        return self.client.service.verifica_tarjeta_bloqueada(n_tarjeta)

    def consultar_intentos(self, n_tarjeta):
        return self.client.service.consulta_intentos(n_tarjeta)

    def consulta_saldo(self, n_tarjeta):
        return self.client.service.consulta_saldo(n_tarjeta)
    
    def consulta_limite(self, n_tarjeta):
        return self.client.service.verifica_limite(n_tarjeta)

    def realiza_pago(self,n_tarjeta, pago):
        return self.client.service.realiza_pago(n_tarjeta, pago)
        