#Crea una clase Alumno con nombre. Crea una clase Curso con nombre y una lista de alumnos, que permita inscribir, remover y listar alumnos.
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.lista_alumnos = []
    
    def inscribir(self, alumno: Alumno):
        self.lista_alumnos.append(alumno)
        print (f"Has inscrito a: {alumno.nombre}, en el curso de {self.nombre_curso}.")

    def remover(self, alumno: Alumno):
        self.lista_alumnos.remove(alumno)
        print (f"Has removido a: {alumno.nombre}, en el curso de {self.nombre_curso}.")

    def listar (self):
        print(f"Listado de Alumnos de {self.nombre_curso}:")
        for alumno in self.lista_alumnos:
            print ({alumno.nombre})
         