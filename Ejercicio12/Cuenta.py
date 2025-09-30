class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def __str__(self):
        return f"{self.titular} | Saldo: ${self.saldo:.2f}"