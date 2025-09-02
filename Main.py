#Ejercicio 1

from ProgramacionOrientadaAObjetoEvaluacionUno.ejercicio1.Clases.biblioteca import Biblioteca
from ProgramacionOrientadaAObjetoEvaluacionUno.ejercicio1.Clases.libro import Libro

Biblioteca1 = Biblioteca()

Biblioteca1.agregar(Libro("Papelucho","Marcela Paz", 15))
Biblioteca1.agregar(Libro("Los python","Carlos Blanco", 15))

Biblioteca1.mostrar()

Biblioteca.prestamo(Biblioteca1, "Papelucho")

Biblioteca1.mostrar()

Biblioteca.devolver(Biblioteca1, "Papelucho")

Biblioteca1.mostrar()

#Ejercicio 2

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio14.Clases.pregunta import Pregunta
from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio2.Clases.grupo import Grupo

grupo1 = Grupo ("Programacion")

grupo1.agrega("Charlie")
grupo1.agrega("Marty")
grupo1.agrega("Charlie")

grupo1.mostrar()

grupo1.quita("Charlie")
grupo1.quita("Lorraine")

grupo1.mostrar()

#Ejercicio 3

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio3.Clases.item import Item
from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio3.Clases.pedido import Pedido

item1 = Item("Computador", 3, 2)

pedido = Pedido(item1)

#Ejercicio 4

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio4.Clases.sensor import Sensor

sensor1 = Sensor

sensor1.agrega(10)
sensor1.agrega(18)
sensor1.agrega(2)

print("Promedio:", sensor1.promedio())
print("Maximo:", sensor1.maximo())
print("Minimo:", sensor1.minimo())

#Ejercicio 5

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio5.Clases.catalogo import Catalogo
from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio5.Clases.pelicula import Pelicula

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

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio6.Clases.auth import Auth

auth1 = Auth()

auth1.registro_usuario("Charli1","contra123")
auth1.registro_usuario("Edgar2","pass456")

print(auth1.acceso("Charli1", "contra123"))
print(auth1.acceso("Edgar2", "Contraseña equivocada"))

#Ejercicio 7

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio7.Clases.agenda import Agenda


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

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio8.Clases import Restaurante

restaurante1 = Restaurante()

restaurante1.agrega_mesa(1, 4)
restaurante1.agrega_mesa(2, 2)

restaurante1.mostrar_estado()

restaurante1.mesas[0].reservar
restaurante1.mesas[0].reservar

restaurante1 = Restaurante()

#Ejercicio 9

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio9.Clases.carrito import Carrito
from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio9.Clases.producto import Producto

producto1 = Producto("Detergente", 20)
producto2 = Producto("Papel", 45)

carrito1 = Carrito()

carrito1.agregar_producto(producto1, 3)
carrito1.agregar_producto(producto2, 2)

total = carrito1.calcular_total()
print(f"Total sin descuento: ${total}")

total_con_dsto = carrito1.aplica_descuento(10)
print(f"Total con descuento aplicado: ${total_con_dsto}")

#Ejercicio 10

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio10.Clases.estudiante1 import Estudiante

estudiante1 = Estudiante("Bastian Guajardo")

estudiante1.agregar_nota("Base de datos", 7.0)
estudiante1.agregar_nota("Programacion", 4.0)
estudiante1.agregar_nota("Back End", 3.0)

estudiante1.mostrar_notas()

promedio = estudiante1.calcular_promedio()
print(f"El promedio del estudiante: {estudiante1.nombre} es: {promedio}")

#Ejercicio 11

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio11.Clases.empresa import Empresa

empresa1 =Empresa()

empresa1.contratar("Andres", 5000)
empresa1.contratar("Daniella", 10000)
empresa1.contratar("Joaquin", 25000)
empresa1.contratar("Anais", 15000)

empresa1.listar_empleados()

empresa1.gasto_total()

#Ejercicio 12

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio12.Clases.banco import Banco

banco1 = Banco()

banco1.abrir_cuenta("Juan", 12000)
banco1.abrir_cuenta("Matias", 2000000)

banco1.mostrar_estado_cuentas()

banco1.transferir("Matias", "Juan", 1000)

banco1.mostrar_estado_cuentas()

#Ejercicio 13

from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio13.Clases.mascota import Mascota
from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio13.Clases.veterinaria import Veterinaria

    veterinaria1 = Veterinaria()

    veterinaria1.registrar_mascota(Mascota("Firulais", "Perro", 5))
    veterinaria1.registrar_mascota(Mascota("Michi", "Gato", 3))
    veterinaria1.registrar_mascota(Mascota("Lola", "Conejo", 2))

    veterinaria1.buscar_por_nombre("Michi")

    veterinaria1.listar_mascotas()

    veterinaria1.edad_promedio()

#Ejercicio 14


from ProgramacionOrientadaAObjetoEvaluacionUno.Ejercicio14.Clases.examen import Examen

examen1 = Examen()

examen1.agregar_preguntar(Pregunta("¿Capital de Chile", "Santiago"))
examen1.agregar_preguntar(Pregunta("¿Capital de Peru", "Lima"))

examen1.listar_preguntas()

print("Total de preguntas: ", examen1.contar_preguntas())
