# Creamos la clase restaurant

class Restaurante:
    def __init__(self):
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f'Mesa "{mesa.numero}" disponible "{mesa.capacidad}" personas ha sido agregada.')

    def reservar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if not mesa.ocupada:
                    mesa.ocupada = True
                    print(f"Mesa '{numero_mesa}' reservada.")
                    return True
                else:
                    print(f"La Mesa '{numero_mesa}' ya está ocupada.")
                    return False
        print(f"No se encontró la Mesa '{numero_mesa}'.")
        return False

    def liberar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.ocupada:
                    mesa.ocupada = False
                    print(f"Mesa '{numero_mesa}' ha sido liberada.")
                    return True
                else:
                    print(f"La Mesa '{numero_mesa}' ya está libre.")
                    return False
        print(f"No se encontró la Mesa '{numero_mesa}'.")
        return False

    def mostrar_estado_mesas(self):
        print("\n--- Estado de las mesas ---")
        for mesa in self.mesas:
            estado = "Ocupada" if mesa.ocupada else "Libre"
            print(f"Mesa '{mesa.numero}': Capacidad para '{mesa.capacidad}' | Estado: '{estado}'.")
            
# Creamos las mesas

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False