from ejercicio14.Clases.pregunta import Pregunta

class Examen:
    def __init__(self,nombre):
        self.nombre = nombre
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
        print("Pregunta agregada al examen.")

    def listar_preguntas(self):
        print("Preguntas en el examen:")
        for pregunta in self.preguntas:
            print(pregunta.enunciado)


    def total_preguntas(self):
        return len(self.preguntas)