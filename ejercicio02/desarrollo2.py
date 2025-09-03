#Clase alumnos

class Alumno:
    def _init_(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
#Clase curso
        
class Curso:
    def _init_(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []

#Agregamos alumnos
        
    def agregar_alumno(self, alumno):
        self.alumnos.aapend(Alumno)
        print(f'Alumno "{Alumno.nombre}" correctamente añadido al curso {self.curso}.')

#Borramos alumnos    
    def retirar_alumno(self, alumno):
        self.alumnos.remove(alumno)
        print(f"alumno '{Alumno.nombre}' eliminado con exito")
        

# lista de alumnos       
    def lista_alumnos(self):
        print(f"los alumnos del curso '{self.nombre_curso}' son {self.alumnos}")

