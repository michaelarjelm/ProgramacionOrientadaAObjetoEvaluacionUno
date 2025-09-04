class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f" Depósito de ${monto} realizado. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f" Retiro de ${monto} realizado. Saldo actual: ${self.saldo}")
            return True
        else:
            print(f" Fondos insuficientes para retirar ${monto}. Saldo actual: ${self.saldo}")
            return False

    def __str__(self):
        return f"Titular: {self.titular} - Saldo: ${self.saldo}"
