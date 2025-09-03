class Pregunta:
    """Clase que representa una pregunta de un examen con su respuesta."""
    def __init__(self, enunciado, respuesta_correcta):
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta
    def __str__(self):
        """Devuelve una representación en cadena del objeto Pregunta."""
        return f"Pregunta: {self.enunciado}\nRespuesta Correcta: {self.respuesta_correcta}"
class Examen:
    """Clase que representa un examen y gestiona sus preguntas."""
    def __init__(self):
        self.preguntas = []
    def agregar_pregunta(self, pregunta):
        """Agrega una pregunta al examen."""
        self.preguntas.append(pregunta)
        print("✅ Pregunta agregada al examen.")
    def listar_preguntas(self):
        """Muestra el listado de todas las preguntas del examen."""
        print("\n📝 Listado de Preguntas del Examen:")
        if not self.preguntas:
            print("El examen no tiene preguntas aún.")
            return
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"--- Pregunta #{i} ---")
            print(pregunta)
    def contar_preguntas(self):
        """Devuelve el número total de preguntas del examen."""
        return len(self.preguntas)