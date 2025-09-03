class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"Cuenta de {cuenta.titular} abierta con éxito.")

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular.lower() == titular.lower():
                return cuenta
 

    def transferir_dinero(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)

        if cuenta_origen.saldo < monto:
            print(f"Error: Saldo insuficiente en la cuenta.")
            return

        cuenta_origen.saldo -= monto
        cuenta_destino.saldo += monto
        print(f"Transferencia exitosa: {monto} transferidos de {titular_origen} a {titular_destino}.")
       

    def mostrar_estado_cuentas(self):
        print("Estado actualizado de las cuentas")
       
        if not self.cuentas:
         print("No hay cuentas registradas en el banco.")
         return
    
        for cuenta in self.cuentas:
            print(f"Titular: {cuenta.titular}, Saldo: {cuenta.saldo}")
    

    