class Nota:
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = calificacion

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota de '{nota.asignatura}' agregada para {self.nombre}.")

    def calcular_promedio(self):
        if not self.notas:
            return 0  

        suma_calificaciones = 0
        for nota in self.notas:
            suma_calificaciones += nota.calificacion
        
        promedio = suma_calificaciones / len(self.notas)
        return promedio

    def mostrar_calificaciones(self):
        
        if not self.notas:
            print("No hay notas registradas.")
            return
            
        for nota in self.notas:
            print(f"Asignatura: {nota.asignatura}, Calificación: {nota.calificacion}")