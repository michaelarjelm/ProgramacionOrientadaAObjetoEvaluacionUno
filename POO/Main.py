#Ejercicio 1


from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio1.Clases import Biblioteca, Libro



Biblioteca1 = Biblioteca()
Biblioteca1.agregar(Libro("Papelucho","Marcela Paz", 15))
Biblioteca1.agregar(Libro("Los python","Carlos Blanco", 15))

Biblioteca1.mostrar()
Biblioteca.prestamo(Biblioteca1, "Papelucho")
Biblioteca1.mostrar()
Biblioteca.devolver(Biblioteca1, "Papelucho")
Biblioteca1.mostrar()

#Ejercicio 2

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio2.Clases import Grupo

grupo1 = Grupo ("Programacion")

grupo1.agrega("Charlie")
grupo1.agrega("Marty")
grupo1.agrega("Charlie")

grupo1.mostrar()

grupo1.quita("Charlie")
grupo1.quita("Lorraine")

grupo1.mostrar()

#Ejercicio 3

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio3.Clases import Item, Pedido

item1 = Item("Computador", 3, 2)

pedido = Pedido(item1)

#Ejercicio 4

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio4 import Sensor

sensor1 = Sensor

sensor1.agrega(10)
sensor1.agrega(18)
sensor1.agrega(2)

print("Promedio:", sensor1.promedio())
print("Maximo:", sensor1.maximo())
print("Minimo:", sensor1.minimo())

#Ejercicio 5

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio5.Clases import Pelicula
from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio5.Clases.catalogo import Catalogo

catalogo1 = Catalogo

p1 = Pelicula("Titanic", "Romance", 1997)
p2 = Pelicula("El Padrino", "Drama", 1972)
p3 = Pelicula("Volver al futuro", "Ciencia ficcion", 1985)

catalogo1.agrega_pelicula(p1)
catalogo1.agrega_pelicula(p2)
catalogo1.agrega_pelicula(p3)

print("Peliculas de Romance:")
romance = catalogo1.filtrar_genero("Romance")
for peli in romance:
    print(f"- {peli.titulo}")
    
print("\nBUscando Titanic:")
pelicula = catalogo1.buscar_titulo("Titanic")
if pelicula:
    print(f"Encontrada: {peli.titulo} - {peli.genero} - {peli.año}")
else:
    print("No se encontro la pelicula")

print("\nCatalogo completo: ")
catalogo1.lista_completa()

#Ejercicio 6

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio6.Clases import Auth

auth1 = Auth()

auth1.registro_usuario("Charli1","contra123")
auth1.registro_usuario("Edgar2","pass456")

print(auth1.acceso("Charli1", "contra123"))
print(auth1.acceso("Edgar2", "Contraseña equivocada"))

#Ejercicio 7

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio7.Clases.agenda import Agenda

agenda1 = Agenda()

agenda1.agrega_contacto("Carlos Blanco", "988881212", "Carlos@gmail.com")
agenda1.agrega_contacto("Josefina Pizarro", "988881313", "Tutito12@gmail.com")

contacto = agenda1.busqueda_contacto("Carlos Blanco")
if contacto:
    print(f"Datos encontrados, Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Correo: {contacto.correo}")
else:
    print("No se encuentra informacion")

agenda1.elimina_contacto("Josefina Pizarro")

agenda1.listar_contactos()

#Ejercicio 8

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio8.Clases import Restaurante

restaurante1 = Restaurante()

restaurante1.agrega_mesa(1, 4)
restaurante1.agrega_mesa(2, 2)

restaurante1.mostrar_estado()

restaurante1.mesas[0].reservar
restaurante1.mesas[0].reservar

restaurante1 = Restaurante()

#Ejercicio 9

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio9.Clases import carrito
from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio9.Clases.carrito import Carrito
from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio9.Clases.producto import Producto

producto1 = Producto("Detergente", 20)
producto2 = Producto("Papel", 45)

carrito1 = Carrito()

carrito1.agregar_producto(producto1, 3)
carrito1.agregar_producto(producto2, 2)

total = carrito.calcular_total()
print(f"Total sin descuento: ${total}")

total_con_dsto = carrito1.aplica_descuento(10)
print(f"Total con descuento aplicado: ${total_con_dsto}")

#Ejercicio 10

from ProgramacionOrientadaAObjetoEvaluacionUno.POO.Ejercicio10.Clases import Estudiante

estudiante1 = Estudiante("Bastian Guajardo")

estudiante1.agregar_nota("Base de datos", 7.0)
estudiante1.agregar_nota("Programacion", 4.0)
estudiante1.agregar_nota("Back End", 3.0)

estudiante1.mostrar_notas()

promedio = estudiante1.calcular_promedio()
print(f"El promedio del estudiante: {estudiante1.nombre} es: {promedio}")

#Ejercicio 11
#Ejercicio 12
#Ejercicio 13
#Ejercicio 14