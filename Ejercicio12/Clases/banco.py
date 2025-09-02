#Clase Banco

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio12.Clases.cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = []
    
    def abrir_cuenta(self, titular, saldo_inicial = 0):
        nueva_cuenta = Cuenta(titular, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
    
    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None
    
    def transferir(self, titular_origen, titular_destino, monto):
        cuenta_origen = self.buscar_cuenta(titular_origen)
        cuenta_destino = self.buscar_cuenta(titular_destino)
        
        if cuenta_origen and cuenta_destino:
            if cuenta_origen.saldo >= monto:
                cuenta_origen.saldo -= monto
                cuenta_destino.saldo += monto
                print(f"Transferencia por {monto}")
            else:
                print("saldo insuficiente")
        else:
            print("La cuenta no existe")
    
    def mostrar_estado_cuenta(self):
        for cuenta in self.cuentas:
            cuenta.mostrar_estado()
        