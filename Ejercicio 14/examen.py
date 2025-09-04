from pregunta import Pregunta

class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, enunciado, respuesta_correcta):
        nueva_pregunta = Pregunta(enunciado, respuesta_correcta)
        self.preguntas.append(nueva_pregunta)
        print("Pregunta agregada.")

    def listar_preguntas(self):
        if not self.preguntas:
            print("No hay preguntas en el examen.")
            return
        print("Preguntas del examen:")
        for i, pregunta in enumerate(self.preguntas, start=1):
            print(f"{i}. {pregunta.enunciado}")

    def total_preguntas(self):
        return len(self.preguntas)
