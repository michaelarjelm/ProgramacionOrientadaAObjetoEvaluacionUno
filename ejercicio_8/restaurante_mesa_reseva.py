class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "Libre"   

class Restaurante:
    def __init__(self):
        self.mesas = []
    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)
    def reservar_mesa(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                if m.estado == "Libre":
                    m.estado = "Ocupada"
                    print(f"La mesa {numero} ha reservada.")
                else:
                    print(f"Mesa {numero} ya se encuentra ocupada.")
                return
        print("No se encontró la mesa.")

    def liberar_mesa(self, numero):
        for m in self.mesas:
            if m.numero == numero:
                if m.estado == "Ocupada":
                    m.estado = "Libre"
                    print(f"Mesa {numero} liberada.")
                else:
                    print(f"Mesa {numero} ya estaba libre.")
                return
        print("No se encontró la mesa.")

    def mostrar_estado(self):
        for m in self.mesas:
            print(f"Mesa {m.numero} __ Con capacidad para: {m.capacidad} personas __ Estado: {m.estado}")
            


        


        
   
