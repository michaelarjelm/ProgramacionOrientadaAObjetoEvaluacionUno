class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        for pregunta in self.preguntas:
            print(pregunta)

    def contar_preguntas(self):
        return len(self.preguntas)
    