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


## ===== desarrollo ejercicio_6 ===== ##
print ("_______Ejercicio SEIS_______")

from ejercicio_6.usuario_autenticacion import Auth
auth = Auth()

auth.registrar("- Samuel", "1234")
auth.registrar("- Camilo", "abcd")

auth.login("Samuel", "1234")  
auth.login("Samuel", "xxxx")  


## ===== desarrollo ejercicio_7 ===== ##

print ("_______Ejercicio SIETE_______")

from ejercicio_7.agenda_contacto import Contacto,Agenda
    
agenda = Agenda()

c1 = Contacto("- Samuel", "12345678", "samuel@mail.com")
c2 = Contacto("- Maria", "987654321", "maria@mail.com")

agenda.agregar_contacto(c1)
agenda.agregar_contacto(c2)

print("Lista de contactos:")
agenda.listar_contactos()

print("-Buscar a Maria:")
agenda.buscar_contacto("Maria")

print("-Eliminar a Samuel:")
agenda.eliminar_contacto("-Samuel")

print("-Lista actualizada:")
agenda.listar_contactos()

## ===== desarrollo ejercicio_8 ===== ##
print ("_______Ejercicio OCHO_______")

from ejercicio_8.restaurante_mesa_reseva import Mesa, Restaurante

restaurante_donSamu = Restaurante()

restaurante_donSamu.agregar_mesa(Mesa(1, 4))
restaurante_donSamu.agregar_mesa(Mesa(2, 2))


restaurante_donSamu.mostrar_estado()

restaurante_donSamu.reservar_mesa(1)
restaurante_donSamu.mostrar_estado()


restaurante_donSamu.liberar_mesa(1)
restaurante_donSamu.mostrar_estado()

## ===== desarrollo ejercicio_9 ===== ##
print ("_______Ejercicio NUEVE_______")
from ejercicio_9.carrito_conDescuento import Producto, Carrito

p1 = Producto("Pan", 1000)
p2 = Producto("Leche", 1500)

carrito = Carrito()

carrito.agregar_producto(p1, 2)  
carrito.agregar_producto(p2, 3)  

print("Total sin descuento:", carrito.calcular_total)


print("Total con 10% de descuento:", carrito.aplicar_descuento)

## ===== desarrollo ejercicio_10 ===== ##
print ("_______Ejercicio DIEZ_______")
from ejercicio_10.estudiante_nota import Estudiante,Nota


estudiante = Estudiante("Samuel")

estudiante.agregar_nota(Nota("Matemáticas", 7))
estudiante.agregar_nota(Nota("Historia", 6))
estudiante.agregar_nota(Nota("Inglés", 5))


print("Notas del estudiante:")
estudiante.mostrar_notas()

print("Promedio:", estudiante.calcular_promedio())

## ===== desarrollo ejercicio_11 ===== ##

print ("_______Ejercicio ONCE_______")

from ejercicio_11.empleado_empresa import Empleado, Empresa


empresa_pc = Empresa()

empresa_pc.contratar(Empleado("- Samuel", 190000))
empresa_pc.contratar(Empleado("- Camilo", 150000))


print("Empleados actuales:")
empresa_pc.listar_empleados()

print("\nGasto total en sueldos:", empresa_pc.gasto_total_sueldos())

## ===== desarrollo ejercicio_12===== ##
print ("_______Ejercicio DOCE_______")
