## ==== desarrollo de ejercicio_1 ==== ##
print ("_______Ejercicio UNO_______")

from  ejercicio_1.libro_biblioteca import Libro, Biblioteca
 
mi_biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad.", "Gabriel Garcia Marquez.", 5)
libro2 = Libro("El corazon delator.", "Edgar Allan Poe.", 7)
libro3 = Libro("La metamorfosis.", "Franz kafka.",3)

mi_biblioteca.agregar(libro1)
mi_biblioteca.agregar(libro2)
mi_biblioteca.agregar(libro3)

mi_biblioteca.prestar("El corazon delator.")

mi_biblioteca.devolver("Cien años de soledad.")

print("-------libros disponibles-------")

mi_biblioteca.mostrar() 
 

## ==== desarrollo de ejercicio_2 ==== ##

print ("_______Ejercicio DOS_______")

from ejercicio_2.alumno_curso import alumno, curso

alumno1 = alumno("- Samuel Morales")
alumno2 = alumno("- Camilo Candia")
alumno3 = alumno("- Joaquin Navarrete")

curso_basico = curso("Serigrafia")
  
curso_basico.inscribir(alumno1)
curso_basico.inscribir(alumno2)
curso_basico.inscribir(alumno3)
curso_basico.remover(alumno2)

curso_basico.listar_alumno()

## ===== desarrollo ejercicio_3 ===== ##


print ("_______Ejercicio TRES_______")

from ejercicio_3.pedido_item import Pedido, Item


item1 = Item("Papas en tarro", 1900, 3)
item2 = Item("Ramitas de queso", 1000, 2)
item3 = Item("Refresco de cola", 1500, 1 )


pedido1 = Pedido()
pedido1.agregaritem(item1)
pedido1.agregaritem(item2)
pedido1.agregaritem(item3)

print("Total del pedido:", pedido1.totalpedido())


## ===== desarrollo ejercicio_4 ===== ##

s1= Sensor("Temperatura")

s1.registrar(-10)
s1.registrar(25)
s1.registrar(30)

s1.promedio()
s1.maximo()
s1.minimo()
