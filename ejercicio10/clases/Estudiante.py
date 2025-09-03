# creamos la clase estudiante, con nombre y notas 
from ejercicio10.clases.Nota import Nota

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, asignatura, calificacion):
        self.notas.append(Nota(asignatura, calificacion))

    def promedio(self):
        if not self.notas:
            return 0
        return sum(n.calificacion for n in self.notas) / len(self.notas)

    def mostrar_notas(self):
        for n in self.notas:
            print(n)
        print("Tu Promedio es:", self.promedio())
