#  Crea una clase Estudiante con nombre y una lista 
# de notas. Agrega métodos para añadir una nota, calcular el promedio y mostrar todas las 
# calificaciones. 
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
        
    def agregar_nota(self, nota):
        self.notas.append(nota)
        
    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.calificacion for nota in self.notas)
        return total / len(self.notas)
    
    def mostrar_notas(self):
        for nota in self.notas:
            print(f"Asignatura: {nota.asignatura}, Calificación: {nota.calificacion}")