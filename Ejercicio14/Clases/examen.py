#Clase Examen
class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"{i}. {pregunta.enunciado}")

    def contar_preguntas(self):
        return len(self.preguntas)
