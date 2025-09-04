from ejercicio8.Clases.mesa import Mesa

class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesas(self, mesa):
        self.mesas.append(mesa)
        print("Mesa agregada")

    def reservar(self, numero):
        for mesa in self.mesas:
         if mesa.numero == numero:
            if mesa.estado == "Libre":
                mesa.estado = "Ocupada"
                print(f"Mesa {numero} ha sido reservada")
            else:
                print(f"Mesa {numero} ocupada")
            return
        print(f"No existe la mesa {numero}")

    def liberar(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                if mesa.estado == "Ocupada":
                    mesa.estado = "Libre"
                    print(f"Mesa {numero} ha sido liberada")
                else:
                    print(f"Mesa {numero} ya estaba libre")
                return
        print(f"No existe la mesa {numero}")

    def mostrar_estado(self):
        if not self.mesas:
            print("No hay mesas registradas")
        else:
            print("Estado de las mesas:")
            for mesa in self.mesas:
                print(f"Mesa {mesa.numero}: {mesa.estado}-Capacidad: {mesa.capacidad} personas ")