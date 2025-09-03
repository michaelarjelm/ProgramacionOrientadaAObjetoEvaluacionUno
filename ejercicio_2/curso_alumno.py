class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Alumno: {self.nombre}"


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []  # Lista para almacenar objetos Alumno

    def inscribir_alumno(self, alumno):
        if isinstance(alumno, Alumno):
            if alumno not in self.alumnos:
                self.alumnos.append(alumno)
                print(f"'{alumno.nombre}' inscrito en el curso '{self.nombre}'.")
            else:
                print(f"'{alumno.nombre}' ya está inscrito en el curso '{self.nombre}'.")
        else:
            print("Solo se pueden inscribir objetos de tipo Alumno.")

    def remover_alumno(self, alumno):
        if isinstance(alumno, Alumno):
            if alumno in self.alumnos:
                self.alumnos.remove(alumno)
                print(f"'{alumno.nombre}' removido del curso '{self.nombre}'.")
            else:
                print(f"'{alumno.nombre}' no está inscrito en el curso '{self.nombre}'.")
        else:
            print("Solo se pueden remover objetos de tipo Alumno.")

    def listar_alumnos(self):
        if not self.alumnos:
            print(f"El curso '{self.nombre}' no tiene alumnos inscritos.")
            return
        print(f"\n--- Alumnos inscritos en '{self.nombre}' ---")
        for alumno in self.alumnos:
            print(alumno)
        print("--------------------------------------")

    def __str__(self):
        return f"Curso: {self.nombre} ({len(self.alumnos)} alumnos)"
