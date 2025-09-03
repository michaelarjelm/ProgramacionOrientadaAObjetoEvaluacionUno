class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def mostrar_info(self):
        return "Titular: " + self.titular + " | Saldo: $" + str(self.saldo)
    
    