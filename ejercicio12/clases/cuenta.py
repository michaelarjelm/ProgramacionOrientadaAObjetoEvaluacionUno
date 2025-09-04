# Crea una clase Cuenta con titular y saldo.
class Cuenta:
    def __init__(self, titular, saldo: float = 0.0):
        self.titular = titular
        self.saldo = saldo  
        print(f"Cuenta creada para {self.titular} con saldo inicial de ${self.saldo:.2f}")  
              
    