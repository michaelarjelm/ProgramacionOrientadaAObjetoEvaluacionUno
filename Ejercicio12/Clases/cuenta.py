#Clase Cuenta
class Cuenta:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
    def mostrar_estado(self):
        print(f"Titular: {self.titular} - Saldo:  ${self.saldo}")