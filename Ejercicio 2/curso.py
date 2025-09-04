from alumno import Alumno

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, nombre_alumno):
        # Evitar inscribir alumnos duplicados
        if any(alumno.nombre == nombre_alumno for alumno in self.alumnos):
            print(f"El alumno '{nombre_alumno}' ya está inscrito en el curso.")
            return False
        nuevo_alumno = Alumno(nombre_alumno)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno '{nombre_alumno}' inscrito en el curso '{self.nombre}'.")
        return True

    def remover_alumno(self, nombre_alumno):
        for alumno in self.alumnos:
            if alumno.nombre == nombre_alumno:
                self.alumnos.remove(alumno)
                print(f"Alumno '{nombre_alumno}' removido del curso '{self.nombre}'.")
                return True
        print(f"Alumno '{nombre_alumno}' no encontrado en el curso.")
        return False

    def listar_alumnos(self):
        if not self.alumnos:
            print(f"No hay alumnos inscritos en el curso '{self.nombre}'.")
            return
        print(f"Alumnos inscritos en el curso '{self.nombre}':")
        for alumno in self.alumnos:
            print(f"- {alumno}")
