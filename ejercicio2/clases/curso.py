
class Curso:
        def __init__(self,nombre_curso):
                self.nombre_curso = nombre_curso
                self.lista_alumnos = []


        def inscribir_alumno(self,alumno):
                self.lista_alumnos.append(alumno)
                print(f"El alumno {alumno} ha sido ingresado al curso {self.nombre_curso}.")


        def listado_alumnos(self):
                print(f"Curso {self.nombre_curso}")
                for alumnos in self.lista_alumnos:
                        print(alumnos)

        
        def quitar_alumno(self):
                while True:
                        nombre_completo = input("ingresa el nombre completo del alumno a quitar de la lista : ").strip()
                        for alumno in self.lista_alumnos:
                                if nombre_completo.lower() == f"{alumno.nombres} {alumno.apellidos}".lower():
                                        self.lista_alumnos.remove (alumno)
                                        print(f"el alumno {alumno} ha sido retirado del curso.")
                                        return
                        else:
                                print("Alumno no encontrado. reingrese el nombre completo correctamente.")
