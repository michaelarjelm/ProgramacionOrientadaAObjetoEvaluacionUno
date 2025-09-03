class Nota:
    def __init__(self, asignatura:str, nota:float):
        self.asignatura = asignatura
        self.nota = nota
    def __str__(self):
        return f"{self.asignatura}: {self.nota}"
    
class Estudiante:
    def __init__(self, nombre:str): 
        self.nombre = nombre # Nombre del estudiante
        self.notas = [] # Lista para almacenar las notas del estudiante
    
    def agregarNota(self, nota:Nota): # Agrega una nota al estudiante
        self.notas.append(nota) # Agrega la nota a la lista de notas
        print(f"Nota agregada: {nota}") # Mensaje de confirmación
    
    def promedio(self): # Calcula el promedio de las notas del estudiante
        if not self.notas: 
            return 0 # Si no hay notas, el promedio es 0
        total = sum(n.nota for n in self.notas) # Suma todas las notas
        return total / len(self.notas) # Retorna el promedio (total dividido por la cantidad de notas)
    
    def mostrarNotas(self): # Muestra todas las notas del estudiante
        if not self.notas:
            print("No hay notas registradas.")
            return  # Si no hay notas, muestra un mensaje y retorna 
        for nota in self.notas: # Itera sobre las notas
            print(nota) # Imprime cada nota