class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f"\nMesa N°{mesa.numero_mesa} creada con exito.")

    def reservar_mesa(self, mesa, numero_comensales):
        # corroborar que existan mesas creadas
        if self.mesas:
            if mesa.estado:
                # corroborar que el numero de comensales no supere la capacidad de la mesa y reservarla
                if mesa.capacidad >= numero_comensales:
                    mesa.estado = False
                    print(f"\nMesa N°{mesa.numero_mesa} reservada con exito.")
                # avisar si la mesa no tiene capacidad
                else:
                    print(f"\nMesa N°{mesa.numero_mesa} sin capacidad suficiente para {numero_comensales} personas.")
                    print(f"Capacidad maxima: {mesa.capacidad}")
            # avisar si la mesa ya esta ocupada
            else:
                print(f"\nLa mesa N°{mesa.numero_mesa} ya está reservada")
        else:
            print("\nEl Restaurante no posee mesas")
    
    def liberar_mesa(self, mesa):
        if self.mesas:
            if not mesa.estado:
                mesa.estado = True
                print(f"\nMesa N°{mesa.numero_mesa} liberada.")
            else:
                print(f"La mesa N°{mesa.numero_mesa} está liberada")
        else:
            print("\nEl Restaurante no posee mesas")

    def mostrar_mesas(self):
        if self.mesas:
            print("\n--- Mesas ---")
            for mesa in self.mesas:
                # comprobar el estado de la mesa
                if mesa.estado:
                    print(f"Mesa N°{mesa.numero_mesa} | Estado: Liberada")
                else:
                    print(f"Mesa N°{mesa.numero_mesa} | Estado: Ocupada")
        else:
            print("\nEl Restaurante no posee mesas")