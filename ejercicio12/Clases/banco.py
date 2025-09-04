class Banco:
    def __init__(self,banco):
        self.banco = banco
        self.lista_cuentas = []



    def abrir_cuenta(self,cuenta):
        self.lista_cuentas.append(cuenta)
        print(f"Cuenta agregada: {cuenta.titular} con saldo {cuenta.saldo}")

    
    def buscar_cuenta(self,titular):
        for cuenta in self.lista_cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    def transferir(self, origen, destino, monto):
        if origen.saldo >= monto:
            origen.saldo -= monto
            destino.saldo += monto
            print(f"Transferencia realizada de {origen.titular} a {destino.titular} por monto {monto}")
        else:
            print("No hay suficiente saldo")
 
    def mostrar_estado(self):
        print("Estado cuentas:") 
        for c in self.lista_cuentas:
            print(c.titular, "=>", c.saldo)