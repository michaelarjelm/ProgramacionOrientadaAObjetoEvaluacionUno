#Ejercicio 1

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio1.Ejercicio1Biblioteca import Biblioteca, devolver, prestamo
from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio1.Ejercicio1Libro import Libro


Biblioteca1 = Biblioteca()
Biblioteca1.agregar(Libro("Papelucho","Marcela Paz", 15))
Biblioteca1.agregar(Libro("Los python","Carlos Blanco", 15))

Biblioteca1.mostrar()
prestamo(Biblioteca1, "Papelucho")
Biblioteca1.mostrar()
devolver(Biblioteca1, "Papelucho")
Biblioteca1.mostrar()