# ~ Creamos la clase Alumno
class Alumno:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

# ~ Creamos la clase Curso
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.alumnos = [] # ~ Lista para almacenar los objetos Alumno

# ~ Métodos para la clase curso ദ്ദി/ᐠ｡‸｡ᐟ\
    def inscribirAlumnos(self, alumno):
        self.alumnos.append(alumno)

    def listarAlumnos(self,alumno):
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre}, Edad: {alumno.edad}, ID: {alumno.id}")
    
    def removerAlumnos(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f"Volaste a {alumno.nombre} del curso xd")
        else:
            print("¿Cuál dijistes k era? (ㆆ _ ㆆ)")