class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
    
    def inscribir_alumno(self, nombre_alumno):
        self.alumnos.append(nombre_alumno)
        print(f"\n** {nombre_alumno} agregado al curso '{self.nombre}' con exito **")

    def remover_alumno(self, nombre_alumno):
        if nombre_alumno in self.alumnos:
            self.alumnos.remove(nombre_alumno)
            print(f"\n** Se removio a {nombre_alumno} del curso {self.nombre} **")
        else:
            print(f"\nAlumno '{nombre_alumno}' no está registrado en el curso {self.nombre}")
    
    def listar_alumnos(self):
        if not self.alumnos:
            print("Curso vacio")
        else:
            print(f"\n--- Curso {self.nombre} ---")
            print(f"Numero de alumnos: {len(self.alumnos)}\n")
            for alumno in self.alumnos:
                print(f"* {alumno}")