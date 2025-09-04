class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
    
    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)
        print(f"\n{alumno} agregado al curso '{self.nombre}' con exito")

    def remover_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f"\nSe removio a {alumno} del curso {self.nombre}")
        else:
            print(f"\nAlumno '{alumno}' no está registrado en el curso {self.nombre}")
    
    def listar_alumnos(self):
        if not self.alumnos:
            print("Curso vacio")
        else:
            print(f"\n--- Curso {self.nombre} ---")
            print(f"Numero de alumnos: {len(self.alumnos)}\n")
            for alumno in self.alumnos:
                print(f"* {alumno}")