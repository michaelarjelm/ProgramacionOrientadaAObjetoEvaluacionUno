class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositó {cantidad} a la cuenta de {self.titular}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiró {cantidad} de la cuenta de {self.titular}. Nuevo saldo: {self.saldo}")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a cero.")
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, titular, saldo_inicial=0):
        nueva_cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta abierta para {titular} con saldo inicial de {saldo_inicial}.")

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        print(f"No se encontró ninguna cuenta a nombre de {titular}.")
        return None

    def transferir(self, origen, destino, cantidad):
        cuenta_origen = self.buscar_cuenta(origen)
        cuenta_destino = self.buscar_cuenta(destino)

        if cuenta_origen and cuenta_destino:
            if cantidad > 0 and cuenta_origen.saldo >= cantidad:
                cuenta_origen.retirar(cantidad)
                cuenta_destino.depositar(cantidad)
                print(f"Transferencia de {cantidad} de {origen} a {destino} realizada.")
            elif cantidad <= 0:
                print("La cantidad a transferir debe ser mayor a cero.")
            else:
                print("Saldo insuficiente para la transferencia.")
        else:
            print("Una o ambas cuentas no existen.")

    def mostrar_estado_cuentas(self):
        print("Estado de las cuentas:")
        for cuenta in self.cuentas:
            print(cuenta)
