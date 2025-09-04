# Ejercicio 12 — Banco y Cuentas 
# Crea una clase Cuenta con titular y saldo. Crea una clase Banco con lista de cuentas. Agrega 
# métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar 
# estado de todas las cuentas. 

from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f" Cuenta para {cuenta.titular} abierta con saldo ${cuenta.saldo}.")

    def buscar_cuenta(self, titular):
        for c in self.cuentas:
            if c.titular.lower() == titular.lower():
                return c
        print(f" No se encontró cuenta para {titular}.")
        return None

    def transferir(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)

        if cuenta_origen and cuenta_destino:
            if cuenta_origen.retirar(monto):
                cuenta_destino.depositar(monto)
                print(f" Transferencia de ${monto} de {titular_origen} a {titular_destino} realizada.")
            else:
                print(" No se pudo realizar la transferencia.")

    def mostrar_estado_cuentas(self):
        if not self.cuentas:
            print(" No hay cuentas en el banco.")
        else:
            print("\n--- Estado de las Cuentas ---")
            for c in self.cuentas:
                print(c)
