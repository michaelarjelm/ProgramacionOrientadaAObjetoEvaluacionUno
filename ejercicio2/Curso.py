class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir(self, alumno):
        self.alumnos.append(alumno)
        print(f"Inscrito: {alumno.nombre}")

    def remover(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                self.alumnos.remove(alumno)
                print(f"Removido: {nombre}")
                return
        print(f"Alumno no encontrado: {nombre}")

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre}")
