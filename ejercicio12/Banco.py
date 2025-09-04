# ejercicio12/Banco.py
class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def buscar_cuenta_por_titular(self, titular):
        for c in self.cuentas:
            if c.titular == titular:
                return c
        return None

    def transferir_dinero(self, titular_origen, titular_destino, monto):
        origen = self.buscar_cuenta_por_titular(titular_origen)
        destino = self.buscar_cuenta_por_titular(titular_destino)
        monto = float(monto)
        if origen and destino and monto > 0 and origen.saldo >= monto:
            origen.saldo -= monto
            destino.saldo += monto
            print(f"Transferido {monto} de {titular_origen} a {titular_destino}")
        else:
            print("Transferencia fallida.")

    def mostrar_estado_cuentas(self):
        for c in self.cuentas:
            print(f"Titular: {c.titular}, Saldo: {c.saldo}")