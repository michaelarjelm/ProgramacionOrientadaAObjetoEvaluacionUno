# Creamos la clase Cuenta, con el titular y saldo, el sado tiene que ser 0 ya que a si es como se crea la cuenta bancaria


from ejercicio11.clases import Cuenta


class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, titular, saldo=0):
        nueva = Cuenta(titular, saldo)
        self.cuentas.append(nueva)

    def buscar(self, titular):
        for c in self.cuentas:
            if c.titular.lower() == titular.lower():
                return c
        return None

    def transferir(self, origen, destino, monto):
        c1 = self.buscar(origen)
        c2 = self.buscar(destino)
        if c1 and c2 and c1.retirar(monto):
            c2.depositar(monto)
            return True
        return False

    def mostrar(self):
        for c in self.cuentas:
            print(c)
