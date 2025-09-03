class Mesa:
    """Representa una mesa con su número, capacidad y estado."""
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "libre"  # Estado inicial
    def __str__(self):
        """Devuelve una representación en cadena del estado de la mesa."""
        return f"Mesa {self.numero} (Capacidad: {self.capacidad}) - Estado: {self.estado}"
    def reservar(self):
        """Cambia el estado de la mesa a 'ocupada'."""
        if self.estado == "libre":
            self.estado = "ocupada"
            return True
        return False
    def liberar(self):
        """Cambia el estado de la mesa a 'libre'."""
        if self.estado == "ocupada":
            self.estado = "libre"
            return True
        return False
class Restaurante:
    """Gestiona las mesas y las reservas del restaurante."""
    def __init__(self):
        self.mesas = []
    def agregar_mesa(self, mesa):
        """Agrega una mesa al restaurante."""
        self.mesas.append(mesa)
        print(f"✅ Mesa {mesa.numero} agregada al restaurante.")
    def reservar_mesa(self, capacidad_deseada):
        """Busca y reserva la primera mesa libre que cumpla con la capacidad."""
        for mesa in self.mesas:
            if mesa.estado == "libre" and mesa.capacidad >= capacidad_deseada:
                mesa.reservar()
                print(f"✅ Mesa {mesa.numero} reservada para {capacidad_deseada} personas.")
                return True
        print(f"❌ No hay mesas libres con capacidad para {capacidad_deseada} personas.")
        return False
    def liberar_mesa(self, numero_mesa):
        """Libera una mesa por su número."""
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                if mesa.liberar():
                    print(f"✅ Mesa {numero_mesa} ha sido liberada.")
                    return True
                else:
                    print(f"❌ La Mesa {numero_mesa} ya estaba libre.")
                    return False
        print(f"❌ La Mesa {numero_mesa} no se encuentra en el restaurante.")
        return False
    def mostrar_estado_mesas(self):
        """Muestra el estado de todas las mesas."""
        print("\n📋 Estado actual de las mesas:")
        if not self.mesas:
            print("No hay mesas en el restaurante.")
        else:
            for mesa in self.mesas:
                print(f"- {mesa}")