from Ejercicio12.Cuenta import Cuenta

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def abrir_cuenta(self, titular, saldo_inicial=0):
        # Evitar duplicados por titular
        for c in self.cuentas:
            if c.titular.lower() == titular.lower():
                return False
        self.cuentas.append(Cuenta(titular, saldo_inicial))
        return True

    def buscar_cuenta(self, titular):
        for c in self.cuentas:
            if c.titular.lower() == titular.lower():
                return c
        return None

    def transferir(self, origen, destino, monto):
        cuenta_origen = self.buscar_cuenta(origen)
        cuenta_destino = self.buscar_cuenta(destino)

        if cuenta_origen and cuenta_destino and cuenta_origen.retirar(monto):
            cuenta_destino.depositar(monto)
            return True
        return False

    def mostrar_estado(self):
        return [str(c) for c in self.cuentas] 