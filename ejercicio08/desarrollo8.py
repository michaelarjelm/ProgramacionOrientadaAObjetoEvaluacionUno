class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "libre"
        
class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        
        print(f"Mesa {mesa.numero} con cupos disponibles para {mesa.capacidad} añadida con exito")

    def reservar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa and mesa.estado == "libre":
                mesa.ocupar()
                print(f"Mesa {mesa.numero} reservada.")
                return 
        print(f"No se pudo reservar la mesa {numero_mesa}.")

    def liberar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa and mesa.estado == "ocupada":
                mesa.liberar()
                print(f"Mesa {mesa.numero} liberada.")
                return 
        print(f"No se pudo liberar la mesa {numero_mesa}.")

    def mostrar_estado_mesas(self):
        if not self.mesas:
         print("El restaurante no tiene mesas.")
        return

        for mesa in self.mesas:
            print(f"Mesa {mesa.numero} (Capacidad: {mesa.capacidad}): Estado: {mesa.estado}")