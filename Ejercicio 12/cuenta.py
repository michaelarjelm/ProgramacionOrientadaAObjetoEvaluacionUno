class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad:.2f} realizado a la cuenta de {self.titular}.")
            return True
        print("Cantidad inválida para depósito.")
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado de la cuenta de {self.titular}.")
            return True
        print("Fondos insuficientes o cantidad inválida para retiro.")
        return False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: ${self.saldo:.2f}"
