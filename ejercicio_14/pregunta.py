class Pregunta:
    def __init__(self, enunciado, respuesta_correcta):
        """
        Inicializa una pregunta.

        Args:
            enunciado (str): El enunciado de la pregunta.
            respuesta_correcta (str): La respuesta correcta a la pregunta.
        """
        self.enunciado = enunciado
        self.respuesta_correcta = respuesta_correcta

    def __str__(self):
        """
        Representación en cadena de la pregunta.
        """
        return f"Pregunta: {self.enunciado}\nRespuesta correcta: {self.respuesta_correcta}"


class Examen:
    def __init__(self):
        """
        Inicializa un examen con una lista vacía de preguntas.
        """
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        """
        Agrega una pregunta al examen.

        Args:
            pregunta (Pregunta): El objeto Pregunta a agregar.
        """
        self.preguntas.append(pregunta)
        print("Pregunta agregada al examen.")

    def listar_preguntas(self):
        """
        Lista todas las preguntas del examen.
        """
        if not self.preguntas:
            print("El examen no tiene preguntas.")
        else:
            print("Preguntas del examen:")
            for i, pregunta in enumerate(self.preguntas):
                print(f"Pregunta {i + 1}:\n{pregunta}\n")

    def contar_preguntas(self):
        """
        Cuenta el total de preguntas en el examen.

        Returns:
            int: El número total de preguntas.
        """
        return len(self.preguntas)


if __name__ == "__main__":
    #Crear un examen
    mi_examen = Examen()

    #Crear preguntas
    pregunta1 = Pregunta("¿Cuál es la capital de Francia?", "París")
    pregunta2 = Pregunta("¿Cuál es el resultado de 2 + 2?", "4")
    pregunta3 = Pregunta("¿En qué año se descubrió América?", "1492")

    #Agregar preguntas al examen
    mi_examen.agregar_pregunta(pregunta1)
    mi_examen.agregar_pregunta(pregunta2)
    mi_examen.agregar_pregunta(pregunta3)

    #Listar las preguntas
    mi_examen.listar_preguntas()

    #Contar el total de preguntas
    total_preguntas = mi_examen.contar_preguntas()
    print(f"Total de preguntas en el examen: {total_preguntas}")
