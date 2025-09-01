##Crea una clase Alumno con nombre. 
##Crea una clase Curso con nombre y una lista de alumnos, que permita inscribir, remover y listar alumnos.

## creo la clase alumno
class alumno:
    def __init__(self, nombre):
        self.nombre = nombre
## creo la clase alumno 
class curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir(self, alumno):
        self.alumnos.append(alumno)
        print(f"- Haz inscrito correctamente a {alumno.nombre} al curso {self.nombre}.")
    
    def remover(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print("___________________________________")
            
            print(f"- Se ha removido exitosamente a {alumno.nombre} del curso de {self.nombre}:")
            
            print ("___________________________________")
        
    def listar_alumno(self):
        print(f"- Listado de alumnos en el curso {self.nombre}:")
        if not self.alumnos:
            print("No hay alumno inscrito")
        for alumno in self.alumnos:
            print(f"{alumno.nombre}")



