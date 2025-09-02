#Clase Estudiante

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio10.Clases import Nota


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
        
    def agregar_nota(self, asignatura, calificacion):
        nota = Nota(asignatura, calificacion)
        self.notas.append(nota)
        
    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.calificacion for nota in self.notas)
        return total / len(self.notas)
    
    def mostrar_notas(self):
        for nota in self.notas:
            print(f"Asignatura: {nota.asignatura} - Calificacion: {nota.calificacion}")