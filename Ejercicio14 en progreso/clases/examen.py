# Ejercicio 14 — Examen y Preguntas
# Crea una clase Pregunta con enunciado y respuesta correcta. Crea una clase Examen con una lista
# de preguntas. Agrega métodos para añadir preguntas, listar preguntas y contar el total de
# preguntas del examen.

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

class Examen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        pass

    def listar_preguntas(self):
        pass

    def total_preguntas(self):
        pass