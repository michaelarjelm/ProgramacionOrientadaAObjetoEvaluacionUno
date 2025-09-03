# Crea una clase Pregunta con enunciado y respuesta correcta. Crea una clase Examen con una lista
# de preguntas. Agrega métodos para añadir preguntas, listar preguntas y contar el total de
# preguntas del examen.

class Pregunta:
    def __init__(self, enunciado, respuestaCorrecta):
        self.enunciado = enunciado
        self.respuestaCorrecta = respuestaCorrecta

class Examen:
    def __init__(self):
        self.listaPreguntas = []

    def agregar (self, pregunta: Pregunta):
        self.listaPreguntas.append(pregunta)
        print (f"Has agregado la pregunta: {pregunta.enunciado}")

    def listar(self):
        print("Listado de preguntas del examen:")
        contador = 1
        for pregunta in self.listaPreguntas:
            print (f"{contador}. {pregunta.enunciado} - Respuesta correcta: {pregunta.respuestaCorrecta}")
            contador += 1

    def contarPreguntas (self):
        total = len(self.listaPreguntas)
        print (f"El total de preguntas en el examen es: {total}")
        return total