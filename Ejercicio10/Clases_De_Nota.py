class Nota:
    """Clase que representa una nota de una asignatura."""
    def __init__(self, asignatura, calificacion):
        self.asignatura = asignatura
        self.calificacion = calificacion
class Estudiante:
    """Clase que representa un estudiante y gestiona sus notas."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
    def agregar_nota(self, asignatura, calificacion):
        """Agrega una nueva nota al estudiante."""
        nueva_nota = Nota(asignatura, calificacion)
        self.notas.append(nueva_nota)
        print(f"✅ Nota {calificacion} en '{asignatura}' agregada para {self.nombre}.")
    def calcular_promedio(self):
        """Calcula el promedio de las calificaciones del estudiante."""
        if not self.notas:
            return 0
        total_calificaciones = sum(nota.calificacion for nota in self.notas)
        return total_calificaciones / len(self.notas)
    def mostrar_calificaciones(self):
        """Muestra el listado de todas las notas del estudiante."""
        print(f"\n📋 Calificaciones de {self.nombre}:")
        if not self.notas:
            print("No hay notas registradas.")
            return
        for nota in self.notas:
            print(f"- {nota.asignatura}: {nota.calificacion}")