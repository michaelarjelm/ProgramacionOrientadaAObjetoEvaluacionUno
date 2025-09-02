#Clase Restaurante

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio8.Clases import Mesa

class Restaurante:
    def __init__(self):
        self.mesas = []
    
    def agrega_mesa(self, numero, capacidad):
        mesa = Mesa(numero, capacidad)
        self.mesas.append(mesa)
        
    def mostrar_estado(self):
        for mesa in self.mesa:
            print(f"La mesa es {mesa.numero} (Capacidad: {mesa.capacidad}) - Estado: {mesa.estado} ")