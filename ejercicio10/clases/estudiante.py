from ejercicio10.clases.nota import Nota


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
        
    def añadir_nota(self, asignatura, calificacion):
        nota = Nota(asignatura,calificacion)
        self.notas.append(nota)
        
    
    def calcular_promedio(self):
        if not self.notas:
            return 0
        
        total = sum(nota.calificacion for nota in self.notas)
        return total / len(self.notas)
    
    
    def mostrar_calificaciones(self):
        if not self.notas:
            print(f"{self.nombre} no tiene calificaciones registradas.")
        else:
            print(f"Calificaciones: \n - Alumno: {self.nombre}.")
            for nota in self.notas:
                print(f" - {nota}")
            print(f" - Promedio: {self.calcular_promedio():.2f}")