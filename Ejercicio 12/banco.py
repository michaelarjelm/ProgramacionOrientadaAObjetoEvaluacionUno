from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, titular, saldo_inicial=0):
        if self.buscar_cuenta(titular) is not None:
            print(f"Ya existe una cuenta para el titular {titular}.")
            return False
        nueva_cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta abierta para {titular} con saldo inicial de ${saldo_inicial:.2f}.")
        return True

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None

    def transferir(self, titular_origen, titular_destino, cantidad):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)

        if cuenta_origen is None:
            print(f"No se encontró la cuenta de origen: {titular_origen}.")
            return False
        if cuenta_destino is None:
            print(f"No se encontró la cuenta destino: {titular_destino}.")
            return False
        if cuenta_origen.retirar(cantidad):
            cuenta_destino.depositar(cantidad)
            print(f"Transferencia de ${cantidad:.2f} de {titular_origen} a {titular_destino} realizada.")
            return True
        else:
            print("No se pudo realizar la transferencia por fondos insuficientes.")
            return False

    def mostrar_estado_cuentas(self):
        if not self.cuentas:
            print("No hay cuentas en el banco.")
            return
        print("Estado de todas las cuentas:")
        for cuenta in self.cuentas:
            print(cuenta)
