class Curso:
    def __init__(self, curso):
        self.nombre = curso
        self.lista_alumnos = []

    def inscribir(self, alumno):
        self.lista_alumnos.append(alumno) 
        print(f"Se ha inscrito al alumno {alumno} al curso {self.nombre}")

    def remover(self, nombre_alumno):
        for alumno in self.lista_alumnos:
            if alumno.nombre == nombre_alumno:  
                self.lista_alumnos.remove(alumno)
                print(f"Se ha removido al alumno {alumno} del curso {self.nombre}")
                return
        print(f"El alumno {nombre_alumno} no está inscrito en el curso {self.nombre}")

    def listar_alumnos(self):
        if not self.lista_alumnos:
            print(f"No hay alumnos inscritos en {self.nombre}")
        else:
            print(f"Alumnos inscritos en {self.nombre}:")
            for alumno in self.lista_alumnos:
                print(f"- {alumno}")