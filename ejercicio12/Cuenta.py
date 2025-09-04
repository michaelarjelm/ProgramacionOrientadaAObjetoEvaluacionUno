# ejercicio12/Cuenta.py
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = max(0, float(saldo))