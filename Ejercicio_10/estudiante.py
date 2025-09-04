# Ejercicio 10 — Estudiante y Nota 
# Crea una clase Nota con asignatura y calificación. Crea una clase Estudiante con nombre y una lista 
# de notas. Agrega métodos para añadir una nota, calcular el promedio y mostrar todas las 
# calificaciones. 

from nota import Nota

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []  # Lista de objetos Nota

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f" Nota agregada: {nota}")

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(n.calificacion for n in self.notas) / len(self.notas)

    def mostrar_notas(self):
        if not self.notas:
            print(f" El estudiante {self.nombre} no tiene notas registradas.")
        else:
            print(f"\n--- Notas del estudiante {self.nombre} ---")
            for n in self.notas:
                print(n)
            print(f" Promedio: {self.calcular_promedio():.2f}")
