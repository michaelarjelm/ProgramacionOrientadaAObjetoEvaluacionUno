# Crea una clase Restaurante que permita agregar mesas, reservar, liberar y mostrar estado de todas las mesas.

from .mesa import Mesa  

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
        print(f"Mesa {mesa.numero} agregada al restaurante.")

    def reservar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                if mesa.estado == 'libre':
                    mesa.estado = 'ocupada'
                    print(f"Mesa {numero} ha sido reservada.")
                    return
                else:
                    print(f"Mesa {numero} ya está ocupada.")
                    return
        print(f"Mesa {numero} no encontrada.")

    def liberar_mesa(self, numero):
        for mesa in self.mesas:
            if mesa.numero == numero:
                if mesa.estado == 'ocupada':
                    mesa.estado = 'libre'
                    print(f"Mesa {numero} ha sido liberada al fin.")
                    return
                else:
                    print(f"Mesa {numero} ya está libre, puedes comer aqui.")
                    return
        print(f"Mesa {numero} mmm... lo siento no la enconte.")

    def mostrar_estado_mesas(self):
        if not self.mesas:
            print("No quedan mesas, reserva con anticipacion para la proxima.")
            return
        print(f"Estado de las mesas en el restaurante '{self.nombre}':")
        for mesa in self.mesas:
            print(mesa)
