# ejercicio8/Restaurante.py
class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def reservar(self, numero):
        for m in self.mesas:
            if m.numero == numero: #si el numero de mesa es igual al numero ingresado
                if m.estado == "libre":
                    m.estado = "ocupada"
                    print(f"Reservada mesa {numero}") # para reservar
                else:
                    print(f"Mesa {numero} ya ocupada.")
                return
        print("Mesa no encontrada.")

    def liberar(self, numero):
        for m in self.mesas: #m sera cada mesa en la lista
            if m.numero == numero:
                if m.estado == "ocupada":
                    m.estado = "libre"
                    print(f"Liberada mesa {numero}")
                else:
                    print(f"Mesa {numero} ya libre.")
                return
        print("Mesa no encontrada.")

    def mostrar_estado_mesas(self):
        for m in self.mesas:
            print(f"Mesa {m.numero}: Capacidad {m.capacidad}, Estado {m.estado}") #mostrar estado de cada mesa