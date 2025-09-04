from statistics import mean

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"\nAsignatura '{nota.asignatura}' agregada")

    def calcular_promedio(self):
        if self.notas:
            total_notas = []
            for nota in self.notas:
                total_notas.append(nota.calificacion)
            print(f"\nPromedio de notas: {mean(total_notas):.2f}")
        else:
            print("\nNo tienes notas para promediar")

    def mostrar_calificaciones(self):
        if self.notas:
            print(f"\n--- Estudiante: {self.nombre.capitalize()}  ---\n")
            for asignatura in self.notas:
                print(f"* {asignatura.asignatura:10}: {asignatura.calificacion} ")
        else:
            print("\nNo tienes notas para promediar")