#Crea una clase Cuenta con titular y saldo. Crea una clase Banco con lista de cuentas. Agrega
#métodos para abrir cuenta, buscar cuenta por titular, transferir dinero entre cuentas y mostrar
#estado de todas las cuentas.
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.listaCuentas = []

    def abrirCuenta (self, cuenta: Cuenta):
        self.listaCuentas.append(cuenta)
        print (f" Has abierto una cuenta a nombre de: {cuenta.titular} con un saldo inicial de: ${cuenta.saldo}")

    def buscarCuenta (self, titular):
        for cuenta in self.listaCuentas:
            if cuenta.titular == titular:
                print (f"Cuenta encontrada: Titular: {cuenta.titular}, Saldo: ${cuenta.saldo}")
                return cuenta
        print (f"No se encontró una cuenta a nombre de: {titular}")
        return None

    def transferir (self, titularOrigen, titularDestino, monto):
        cuentaOrigen = self.buscarCuenta(titularOrigen)
        cuentaDestino = self.buscarCuenta(titularDestino)

        if cuentaOrigen and cuentaDestino: #Verifica que las cuentas existam y no retorna None
            if cuentaOrigen.saldo >= monto: #con esto me asgeuro que no sea negativo el saldo
                cuentaOrigen.saldo -= monto #acá se le resta el monto
                cuentaDestino.saldo += monto #acá se le suma el monto
                print (f"Has transferido ${monto} de {titularOrigen} a {titularDestino}")
            else:
                print (f"Saldo insuficiente")
        else:
            print (f"No se pudo completar la transferencia")

    def mostrarEstadoCuentas (self):
        if not self.listaCuentas:
            print("No hay cuentas en el banco.")
            return
        print("Estado de todas las cuentas:")
        for cuenta in self.listaCuentas:
            print (f"Titular: {cuenta.titular}, Saldo: ${cuenta.saldo}")    