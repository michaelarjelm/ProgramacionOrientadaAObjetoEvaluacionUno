class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, titular):
        self.cuentas.append(titular)
        print("\nCuenta registrada con exito")

    def buscar_cuenta(self, titular):
        if self.cuentas:
            if titular in self.cuentas:
                print("\nResultado de la busqueda:")
                print(f"* Titular: {titular.nombre} | Saldo: ${titular.saldo}")
            else:
                print("\nError de busqueda")
                print("La cuenta no esta registrada")
        else:
            print("\nError de busqueda")
            print("No hay cuentas registradas")

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen in self.cuentas:
            if cuenta_origen.saldo - monto >= 0:
                if cuenta_destino in self.cuentas:
                    cuenta_origen.saldo -= monto
                    cuenta_destino.saldo += monto
                    print(f"\n** Transferencia realizada **\n")
                    print(f"Monto: {monto}")
                    print(f"Origen : {cuenta_origen.nombre}")
                    print("-------")
                    print(f"Destinatario: {cuenta_destino.nombre}")
                else:
                    print("\nTransferencia no realizada")
                    print("La cuenta de destino no esta registrada")
            else:
                print("\nTransferencia no realizada")
                print("No tienes fondos suficientes para hacer la transferencia.")
                print(f"Monto disponible: ${cuenta_origen.saldo}")
        else:
            print("\nTransferencia no realizada.")
            print("La cuenta de origen no esta registrada")

    def ver_cuentas(self):
        if self.cuentas:
            print("\n--- Lista de cuentas ---\n")
            for cuenta in self.cuentas:
                print(f"* Cuenta: {cuenta.nombre} | Saldo: ${cuenta.saldo}")
        else:
            print("\nError de visualizacion")
            print("No hay cuentas registradas")
