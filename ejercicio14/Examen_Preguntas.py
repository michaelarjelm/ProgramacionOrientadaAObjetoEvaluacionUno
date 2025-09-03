#Ejercicio 14 — Examen y Preguntas
#Crea una clase Pregunta con enunciado y respuesta correcta. 
#Crea una clase Examen con una lista de preguntas. Agrega métodos para añadir preguntas, listar preguntas y contar el total de preguntas del examen.

class Pregunta:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"Pregunta {i}: {pregunta.enunciado}")

    def contar_preguntas(self):
        return len(self.preguntas)
