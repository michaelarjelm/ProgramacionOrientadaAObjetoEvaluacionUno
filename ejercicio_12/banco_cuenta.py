##Crea una clase Cuenta con titular y saldo. 
##Crea una clase Banco con lista de cuentas. Agrega métodos para abrir cuenta, buscar cuenta por titular, 
##transferir dinero entre cuentas y mostrar estado de todas las cuentas.

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta abierta para {cuenta.titular} con saldo {cuenta.saldo}")

    def buscar_cuenta(self, titular):
        for c in self.cuentas:
            if c.titular == titular:
                return c
        return None

    def transferir(self, de_titular, a_titular, monto):
        cuenta_origen = self.buscar_cuenta(de_titular)
        cuenta_destino = self.buscar_cuenta(a_titular)

        if not cuenta_origen or not cuenta_destino:
            print("Error: alguna cuenta no existe.")
            return

        if cuenta_origen.saldo < monto:
            print("Error: saldo insuficiente.")
            return

        cuenta_origen.saldo -= monto
        cuenta_destino.saldo += monto
        print(f"Transferencia de {monto} de {de_titular} a {a_titular} realizada.")

    def mostrar_cuentas(self):
        for c in self.cuentas:
            print(f"{c.titular} - Saldo: {c.saldo}")
