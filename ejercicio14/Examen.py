class Examen:
    def __init__(self):
        self.preguntas = []

    def anadir_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        for p in self.preguntas:
            print(f"Enunciado: {p.enunciado}, Respuesta: {p.respuesta_correcta}")

    def contar_total_preguntas(self):
        return len(self.preguntas)