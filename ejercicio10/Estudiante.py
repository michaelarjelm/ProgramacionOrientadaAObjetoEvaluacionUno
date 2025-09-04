# ejercicio10/Estudiante.py
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def anadir_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        return sum(n.calificacion for n in self.notas) / len(self.notas) if self.notas else 0

    def mostrar_calificaciones(self):
        for n in self.notas:
            print(f"Asignatura: {n.asignatura}, Calificación: {n.calificacion}")