class Examen:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        """Agrega una nueva pregunta al examen"""
        self.preguntas.append(pregunta)

    def listar_preguntas(self):
        """Lista todas las preguntas del examen"""
        if not self.preguntas:
            return "No hay preguntas registradas en el examen."
        return "\n\n".join(str(pregunta) for pregunta in self.preguntas)

    def contar_total_preguntas(self):
        """Cuenta el total de preguntas del examen"""
        return len(self.preguntas)