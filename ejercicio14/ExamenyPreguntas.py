# Creamos las preguntas
class Pregunta:
    def _init_(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

class Examen:
    def _init_(self):
        self.preguntas = []

    def anadir_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
        print("Pregunta añadida con éxito.")

    def listar_preguntas(self):
        if not self.preguntas:
            print("El examen no tiene preguntas registradas.")
            return

        for pregunta in self.preguntas:
            print("-" * 20)
        
    def contar_preguntas(self):
        total = len(self.preguntas)
        return total