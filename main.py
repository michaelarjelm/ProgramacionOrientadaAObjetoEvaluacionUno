## ==== desarrollo de ejercicio_1 ==== ##
print ("_______Ejercicio UNO_______")

from ejercicio_1.libro_biblioteca import Libro, Biblioteca
 
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

print("EL total del pedido: $", pedido1.totalpedido(), "muchas gracias por tu compra.")


## ===== desarrollo ejercicio_4 ===== ##
print ("_______Ejercicio CUATRO_______")

from ejercicio_4.sensor_mediciones import Sensor

s1 = Sensor("Termico")

s1.registrar(27)
s1.registrar(15)
s1.registrar(-5)

s1.promedio()
s1.maximo()
s1.minimo()


## ===== desarrollo ejercicio 5 ===== ##
print ("_______Ejercicio CINCO_______")

from ejercicio_5.pelicula_catalogo import Pelicula, Catalogo

pelicula1 = Pelicula("Matrix", "Ciencia Ficción", 1999)
pelicula2 = Pelicula("El Padrino", "Drama", 1972)
pelicula3 = Pelicula("Toy Story", "Animación", 1995)

catalogo = Catalogo()
catalogo.agregar_pelicula(pelicula1)
catalogo.agregar_pelicula(pelicula2)
catalogo.agregar_pelicula(pelicula3)

print("Todas las películas:")
catalogo.listar_todas()

print(" Buscar por título 'Matrix:")
for p in catalogo.buscar_por_titulo("Matrix"):
    print(p)

print(" Filtrar por género 'Drama:")
for p in catalogo.filtrar_por_genero("Drama"):
    print(p)


