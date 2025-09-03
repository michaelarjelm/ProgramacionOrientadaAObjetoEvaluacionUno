#Ejercicio 2 — Alumno y Curso
#Crea una clase Alumno con nombre. 
#Crea una clase Curso con nombre y una lista de alumnos, que permita inscribir, remover y listar alumnos.

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)

    def remover_alumno(self, alumno):
        self.alumnos.remove(alumno)

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.nombre)
            
