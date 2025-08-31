

from ejercicio2.clases.Alumno import Alumno


class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos: list[Alumno] = []

    def inscribir(self, alumno: Alumno) -> None:
        self.alumnos.append(alumno)

    def remover(self, nombre: str) -> None:
        
        self.alumnos = [a for a in self.alumnos if a.nombre != nombre]

    def listar(self) -> list[str]:
        
        return [a.nombre for a in self.alumnos]