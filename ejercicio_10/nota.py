class Nota:
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = calificacion

    def __str__(self):
        return f"{self.asignatura}: {self.calificacion}"


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.calificacion for nota in self.notas)
        return total / len(self.notas)

    def mostrar_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for nota in self.notas:
            print(nota)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear notas
    nota1 = Nota("Matemáticas", 8.5)
    nota2 = Nota("Historia", 7.0)
    nota3 = Nota("Ciencias", 9.0)

    # Crear estudiante
    estudiante1 = Estudiante("Ana")

    # Agregar notas al estudiante
    estudiante1.agregar_nota(nota1)
    estudiante1.agregar_nota(nota2)
    estudiante1.agregar_nota(nota3)

    # Mostrar calificaciones
    estudiante1.mostrar_calificaciones()

    # Calcular y mostrar el promedio
    promedio = estudiante1.calcular_promedio()
    print(f"Promedio: {promedio}")
