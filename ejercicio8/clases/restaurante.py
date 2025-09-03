class Restaurante:
    def __init__(self):
            self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)


    def reservar_mesa(self, numero_mesa):
        mesa_encontrada = None
        
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                mesa_encontrada = mesa
                break

        if mesa_encontrada:
            if mesa_encontrada.estado == "libre":
                mesa_encontrada.estado = "ocupada"
                print(f"mesa {numero_mesa} reservada exitosamente.")
            else:
                print(f"La mesa {numero_mesa} ya está ocupada.")
        else:
            print(f"La mesa {numero_mesa} no existe.")


    def liberar_mesa(self, numero_mesa):
        
        mesa_encontrada = None
        
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                mesa_encontrada = mesa
                break
        if mesa_encontrada:
            if mesa_encontrada.estado == "ocupada":
                mesa_encontrada.estado = "libre"
                print(f"mesa {numero_mesa} liberada exitosamente.")
            else:
                print(f"La mesa {numero_mesa} está disponible.")
        else:
            print(f"La mesa {numero_mesa} no existe.")
        
        
    def mostrar_estado_mesas(self):
        if not self.mesas:
            print("No hay mesas registradas en el restaurante.")
            return

        print("Estado de las mesas")
        for mesa in self.mesas:
            print(mesa)
        