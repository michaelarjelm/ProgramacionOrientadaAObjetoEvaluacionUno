# Creacion de los alumnos
class Alumno:
    def __init__(self, nombre, apellido, numerolista):
        self.nombre = nombre
        self.apellido = apellido
        self.numerolista = numerolista
    
    def Preguntar(self):
        return (f'{self.nombre} {self.apellido}, Número de lista: {self.numerolista}')

# Creacion curso
class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []
        
    def AgregarAlumno(self, alumno):
        self.alumnos.append(alumno)
        print(f'Alumno "{alumno.nombre}" "{alumno.apellido}" inscrito en el curso.')
    
    def RetirarAlumno(self, alumno):
        try:
            self.alumnos.remove(alumno)
            print(f'Alumno "{alumno.nombre}" "{alumno.apellido}" retirado del curso.')
        except ValueError:
            print(f'El alumno "{alumno.nombre}" no está en el curso.')
        
    def ListaAlumnos(self):
        print("Alumnos en el curso:")
        for alumno in self.alumnos:
            print(alumno.Preguntar())