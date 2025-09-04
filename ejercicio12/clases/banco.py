#Crea una clase Banco con lista de cuentas. Agrega 
# métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar 
# estado de todas las cuentas.
class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def buscar_cuenta_por_titular(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    def transferir_dinero(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta_por_titular(titular_origen)
        cuenta_destino = self.buscar_cuenta_por_titular(titular_destino)

        if cuenta_origen and cuenta_destino and cuenta_origen.saldo >= monto:
            cuenta_origen.saldo -= monto
            cuenta_destino.saldo += monto
            return True
        return False

    def mostrar_estado_cuentas(self):
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: ${cuenta.saldo:.2f}")