# Ejercicio 12 — Banco y Cuentas
# Crea una clase Cuenta con titular y saldo. Crea una clase Banco con lista de cuentas. Agrega
# métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar
# estado de todas las cuentas.

class Cuenta:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, titular):
        self.cuentas.append(titular)
        pass

    def buscar_cuenta(self, titular):
        if titular in self.cuentas:
            print(f"{titular.nombre} {titular.saldo}")
        else:
            print('noin')

    def transferir(self, cuenta_origen, cuenta_destino, monto):
        if cuenta_origen in self.cuentas:
            if cuenta_origen - monto >= 0:
                if cuenta_destino in self.cuentas:
                    cuenta_origen -= monto
                    cuenta_destino += monto
                    print(f"\n** Transferencia realizada **\n")
                    print(f"Monto: {monto}")
                    print(f"Origen : {cuenta_origen.nombre}")
                    print("\n-------\n")
                    print(f"Destinatario: {cuenta_destino.nombre}")
                else:
                    print("La cuenta de destino no esta registrada")
            else:
                print("\nNo tienes fondos suficientes para hacer la transferencia.")
                print(f"Monto disponible: ${cuenta_origen.saldo}")
        else:
            print("La cuenta de origen no esta registrada")


    def ver_cuentas(self):
        if self.cuentas:
            print("\n--- Lista de cuentas ---")
            for cuenta in self.cuentas:
                print(f"")
