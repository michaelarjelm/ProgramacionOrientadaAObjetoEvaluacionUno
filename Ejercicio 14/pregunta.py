class Pregunta:
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

    def __str__(self):
        return f"Pregunta: {self.enunciado}"
