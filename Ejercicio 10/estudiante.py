from nota import Nota

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, asignatura, calificacion):
        nueva_nota = Nota(asignatura, calificacion)
        self.notas.append(nueva_nota)
        print(f"Nota agregada: {asignatura} - {calificacion}")

    def calcular_promedio(self):
        if not self.notas:
            print("No hay notas para calcular promedio.")
            return 0
        total = sum(n.calificacion for n in self.notas)
        promedio = total / len(self.notas)
        return promedio

    def mostrar_calificaciones(self):
        if not self.notas:
            print("No hay calificaciones registradas.")
            return
        print(f"Calificaciones de {self.nombre}:")
        for nota in self.notas:
            print(nota)
