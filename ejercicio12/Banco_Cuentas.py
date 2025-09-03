#Ejercicio 12 — Banco y Cuentas
#Crea una clase Cuenta con titular y saldo. Crea una clase Banco con lista de cuentas. 
#Agrega métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar estado de todas las cuentas.

class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    def transferir_dinero(self, de_titular, a_titular, monto):
        cuenta_de = self.buscar_cuenta(de_titular)
        cuenta_a = self.buscar_cuenta(a_titular)
        if cuenta_de and cuenta_a and cuenta_de.saldo >= monto:
            cuenta_de.saldo -= monto
            cuenta_a.saldo += monto
            return True
        return False

    def mostrar_estado_cuentas(self):
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: {cuenta.saldo}")
