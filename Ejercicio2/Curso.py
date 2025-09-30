class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir(self, alumno):
        self.alumnos.append(alumno)
        print(f"Alumno inscrito: {alumno.nombre}")

    def remover(self, nombre_alumno):
        for alumno in self.alumnos:
            if alumno.nombre == nombre_alumno:
                self.alumnos.remove(alumno)
                print(f"Alumno removido: {nombre_alumno}")
                return
        print(f"Alumno no encontrado: {nombre_alumno}")

    def listar(self):
        print(f"Alumnos en el curso {self.nombre}:")
        if not self.alumnos:
            print("No hay alumnos inscritos.")
        else:
            for alumno in self.alumnos:
                print(" ", alumno.nombre)