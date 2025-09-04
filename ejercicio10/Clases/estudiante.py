class Estudiante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.notas = []


    def agregar_notas(self,nota):
        self.notas.append(nota)
        print(f"{self.nombre} su nota ha sido agregada")
        


    def calcular_promedio(self):
       if self.notas == 0:
        print("No hay calificaciones")
       else:
        promedio =sum(nota.calificacion for nota in self.notas) / len(self.notas)
        return promedio
       
       
        
    def mostrar_calificaciones(self):
        print(f"{self.nombre}, estas son tus notas:")
        for nota in self.notas:
            print(f"- {nota}")
