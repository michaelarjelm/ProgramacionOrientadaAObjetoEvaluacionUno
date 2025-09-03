class Alumno:
    """Clase que representa a un alumno con un nombre."""
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        """Devuelve una representación en cadena del alumno."""
        return self.nombre
class Curso:
    """Clase que representa un curso con una lista de alumnos."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
    def inscribir_alumno(self, alumno):
        """Inscribe un alumno en el curso."""
        self.alumnos.append(alumno)
        print(f"✅ Alumno '{alumno.nombre}' inscrito en el curso '{self.nombre}'.")
    def remover_alumno(self, nombre_alumno):
        """Remueve un alumno del curso por su nombre."""
        for alumno in self.alumnos:
            if alumno.nombre == nombre_alumno:
                self.alumnos.remove(alumno)
                print(f"✅ Alumno '{nombre_alumno}' removido del curso '{self.nombre}'.")
                return
        print(f"❌ No se encontró al alumno '{nombre_alumno}' en el curso '{self.nombre}'.")
    def listar_alumnos(self):
        """Muestra el listado de alumnos del curso."""
        print(f"\n📋 Alumnos en el curso de '{self.nombre}':")
        if not self.alumnos:
            print("No hay alumnos inscritos en este curso.")
        else:
            for alumno in self.alumnos:
                print(f"- {alumno.nombre}")