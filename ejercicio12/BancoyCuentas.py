class Cuenta:
    def _init_(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class Banco:
    def _init_(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"\nCuenta de '{cuenta.titular}' fue abierta con éxito.")

    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular.lower() == titular.lower():
                return cuenta

    def transferir_dinero(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)

        if cuenta_origen.saldo < monto:
            print(f"\n Error: Saldo insuficiente en la cuenta.")
            return
        cuenta_origen.saldo -= monto
        cuenta_destino.saldo += monto
        print(f"\n Transferencia exitosa! '{monto}' transferido de '{titular_origen}' a '{titular_destino}'.")
       
    def estado_cuentas(self):
        print(f"\n Estado actualizado de las cuentas")
       
        if not self.cuentas:
         print(f"\n No hay cuentas registradas en el banco.")
         return
    
        for cuenta in self.cuentas:
            print(f"\n Titular: '{cuenta.titular}', Saldo: '{cuenta.saldo}'.")