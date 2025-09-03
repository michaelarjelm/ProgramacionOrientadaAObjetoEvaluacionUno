from ejercicio12.clases.cuenta import Cuenta


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def abrir_cuenta(self, titular, saldo_inicial=0):
        nueva_cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        print("Cuenta abierta para " + titular + " con saldo inicial $" + str(saldo_inicial))
        return nueva_cuenta

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular.lower() == titular.lower():
                return cuenta
        return None

    def transferir(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)

        if cuenta_origen is None or cuenta_destino is None:
            print("Una o ambas cuentas no existen.")
            return

        if monto > 0 and cuenta_origen.saldo >= monto:
            cuenta_origen.saldo -= monto
            cuenta_destino.saldo += monto
            print("Transferencia de $" + str(monto) + 
                " realizada de " + titular_origen + " a " + titular_destino + ".")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_estado(self):
        if len(self.cuentas) == 0:
            print("No hay cuentas registradas en el banco.")
        else:
            print("Estado de cuentas en el banco " + self.nombre + ":")
            for cuenta in self.cuentas:
                print("- " + cuenta.mostrar_info())