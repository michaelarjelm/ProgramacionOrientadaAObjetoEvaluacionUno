# Crea una clase Nota con asignatura y calificación. Crea una clase Estudiante con nombre y una lista de notas. Agrega métodos para añadir una nota, calcular el promedio y mostrar todas las calificaciones.
class Nota:
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = calificacion

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaNotas = []

    def agregarNota (self, nota: Nota):
        self.listaNotas.append(nota)
        print (f"Has agregado la nota de {nota.calificacion} en la asignatura de: {nota.asignatura}")

    def promedio (self):
        if not self.listaNotas:
            print("No hay notas registradas.")
            return 0
        total = sum(nota.calificacion for nota in self.listaNotas)
        promedio = total / len(self.listaNotas)
        print (f"El promedio de las notas es: {promedio}")
        return promedio

    def mostrarNotas (self):
        if not self.listaNotas:
            print("No hay notas registradas.")
            return
        print(f"Notas del estudiante {self.nombre}:")
        for nota in self.listaNotas:
            print (f"Asignatura: {nota.asignatura}, Calificación: {nota.calificacion}")