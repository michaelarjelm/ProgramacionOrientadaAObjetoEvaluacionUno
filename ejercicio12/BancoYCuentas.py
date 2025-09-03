class Cuenta:

    def __init__(self, titular: str, numeroCuenta: str, saldo: float = 0):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo


    def depositar(self, monto: float):
        self.saldo += monto # ~ Deposita el monto indicado

    def retirar(self, monto: float) -> bool:
        if self.saldo >= monto: # ~ Verifica fondos suficientes (no permite sobregiros)
            self.saldo -= monto # ~ Retira el monto indicado
            return True # ~ Retiro exitoso    
        return False # ~ Fondos insuficientes
    

    def __str__(self):
        return f"Cuenta  nro. {self.numeroCuenta} - Saldo disponible: ${self.saldo:,.2f}"

class Banco:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cuentas = {} 

    def abrirCuenta(self, cuenta: Cuenta):
        self.cuentas[cuenta.numeroCuenta] = cuenta
        print(f"Nueva cuenta {cuenta.numeroCuenta} para {cuenta.titular}.")

    def mostrarCuentas(self):
        for cuenta in self.cuentas.values():
            print(f"  - {cuenta}")
