
from ejercicio14.clases.pregunta import Pregunta

class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []

    def agregar_pregunta(self, enunciado, respuesta_correcta):
        self.preguntas.append(Pregunta(enunciado, respuesta_correcta))
        print(f"Pregunta agregada: {enunciado}")

    def listar_preguntas(self):
        if not self.preguntas:
            print(f"No hay preguntas en el examen '{self.nombre}'.")
        else:
            print(f"Preguntas del examen '{self.nombre}':")
            for idx, pregunta in enumerate(self.preguntas, start=1):
                print(f"{idx}. {pregunta}")

    def contar_preguntas(self):
        total = len(self.preguntas)
        print(f"Total de preguntas en el examen '{self.nombre}': {total}")
        return total