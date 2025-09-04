from .alumno import Alumno
class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos = []
    
# crear metodo para inscribir alumno        
    def inscribir_alumno(self, alumno:Alumno):
        self.alumnos.append(alumno)
        print(f'Alumno {alumno} inscrito en el curso {self.nombre}.')
        return self.alumnos

# crear metodo para remover alumno  
    def remover_alumno(self, alumno:Alumno):
        self.alumnos.remove(alumno)
        print(f'Alumno {alumno} a sido removido del curso {self.nombre}.')
        return self.alumnos
    
#crear metodo para listar alumnos
    def listar_alumnos(self):
        print(f'Alumnos inscritos en el curso {self.nombre}:')
        for alumno in self.alumnos:
            print(f'- {alumno}')
        return self.alumnos
    