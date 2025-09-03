class Pregunta:
    def __init__(self, enunciado, respuestaCorrecta):
        self.enunciado = enunciado
        self.respuestaCorrecta = respuestaCorrecta
        
    def __str__(self):
        return self.enunciado

#--------------------------------------------------

class Examen:
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregarPregunta(self, pregunta: Pregunta):
        self.preguntas.append(pregunta)
        print("Pregunta añadida al examen.")

    def listarPreguntas(self):
        if not self.preguntas:
            print("El examen no tiene preguntas.")
        else:
            for i, pregunta in enumerate(self.preguntas, 1): # ~ Empieza la numeración en 1 (enumerate)
                print(f"  {i}. {pregunta}") # ~ Llama al __str__ de Pregunta

    def totalPreguntas(self):
        total = len(self.preguntas)
        print(f"El examen consta de {total} preguntas.")
