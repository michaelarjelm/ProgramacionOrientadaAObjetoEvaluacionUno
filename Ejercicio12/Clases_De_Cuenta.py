class Cuenta:
    """Clase que representa una cuenta bancaria con titular y saldo."""
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, monto):
        """Añade un monto al saldo de la cuenta."""
        self.saldo += monto
        print(f"✅ Depósito de ${monto:.2f} realizado en la cuenta de {self.titular}.")
    def retirar(self, monto):
        """Retira un monto de la cuenta si hay saldo suficiente."""
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"✅ Retiro de ${monto:.2f} realizado de la cuenta de {self.titular}.")
            return True
        else:
            print(f"❌ Saldo insuficiente en la cuenta de {self.titular}.")
            return False
    def __str__(self):
        """Devuelve una representación en cadena del objeto Cuenta."""
        return f"Titular: {self.titular} | Saldo: ${self.saldo:.2f}"
class Banco:
    """Clase que gestiona una lista de cuentas bancarias."""
    def __init__(self):
        self.cuentas = []
    def abrir_cuenta(self, titular, saldo_inicial=0.0):
        """Abre una nueva cuenta en el banco."""
        nueva_cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        print(f"✅ Cuenta abierta para '{titular}' con un saldo inicial de ${saldo_inicial:.2f}.")
    def buscar_cuenta(self, titular):
        """Busca y devuelve una cuenta por el nombre de su titular."""
        for cuenta in self.cuentas:
            if cuenta.titular.lower() == titular.lower():
                return cuenta
        return None
    def transferir(self, origen_titular, destino_titular, monto):
        """Transfiere dinero entre dos cuentas."""
        cuenta_origen = self.buscar_cuenta(origen_titular)
        cuenta_destino = self.buscar_cuenta(destino_titular)
        if not cuenta_origen:
            print(f"❌ Error: La cuenta de origen '{origen_titular}' no existe.")
            return False
        if not cuenta_destino:
            print(f"❌ Error: La cuenta de destino '{destino_titular}' no existe.")
            return False
        if cuenta_origen.retirar(monto):
            cuenta_destino.depositar(monto)
            print(f"✅ Transferencia de ${monto:.2f} de {origen_titular} a {destino_titular} completada.")
            return True
        else:
            return False
    def mostrar_estado_cuentas(self):
        """Muestra el estado de todas las cuentas en el banco."""
        print("\n🏦 Estado actual de las cuentas:")
        if not self.cuentas:
            print("No hay cuentas registradas.")
        else:
            for cuenta in self.cuentas:
                print(f"- {cuenta}")