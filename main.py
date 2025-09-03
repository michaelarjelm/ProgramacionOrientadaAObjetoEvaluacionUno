from Ejercicio1.clases.libro import Libro
from Ejercicio1.clases.biblioteca import Biblioteca
from Ejercicio2.clases.alumno import Alumno
from Ejercicio2.clases.curso import Curso
from Ejercicio3.clases.item import Item
from Ejercicio3.clases.pedido import Pedido
from Ejercicio4.clases.sensor import Sensor
from Ejercicio5.clases.catalogo import Catalogo
from Ejercicio5.clases.pelicula import Pelicula
from Ejercicio6.clases.auth import Auth
from Ejercicio6.clases.usuario import Usuario
from Ejercicio7.clases.agenda import Agenda
from Ejercicio7.clases.contacto import Contacto
from Ejercicio8.clases.mesa import Mesa
from Ejercicio8.clases.restaurante import Restaurante
from Ejercicio9.clases.carrito import Carrito
from Ejercicio9.clases.producto import Producto 
from Ejercicio10.clases.estudiante import Estudiante
from Ejercicio10.clases.nota import Nota
from Ejercicio11.clases.empleado import Empleado
from Ejercicio11.clases.empresa import Empresa
from Ejercicio12.clases.banco import Banco
from Ejercicio12.clases.cuenta import Cuenta
# from Ejercicio13.clases.mascota import
# from Ejercicio13.clases.veterinaria import
# from Ejercicio14.clases.examen import
# from Ejercicio14.clases.pregunta import



print("\n\t==== Ejercicio 1: Libro y Biblioteca ====")

libro1 = Libro("Nubes de talco", "Amanda Baeza", 5)
libro2 = Libro("Peklo", "Sukinapan", 7)
libro3 = Libro("Tekkonkinkreet", "Taiyo Matsumoto", 3)

bibliobus = Biblioteca("Bibliobus")

bibliobus.agregar_libro(libro1)
bibliobus.agregar_libro(libro2)
print("--------------------------------")
bibliobus.prestamo(libro1, 3)
print("--------------------------------")
bibliobus.devolucion(libro1, 2)
print("--------------------------------")
bibliobus.listar_libros()

print("\n\t==== Ejercicio 2: Alumno y Curso ====")

alumno1 = Alumno("Alondra Gonzalez")
alumno2 = Alumno("Rovin Gatica")
alumno3 = Alumno("Diego Foster")

curso = Curso("Ilustracion")

curso.inscribir_alumno(alumno1)
curso.inscribir_alumno(alumno2)
print("--------------------------------")
curso.listar_alumnos()
print("--------------------------------")
curso.remover_alumno(alumno3)
curso.remover_alumno(alumno1)

print("\n\t==== Ejercicio 3: Item y Pedido ====")

item1 = Item("lapiz", 1200, 6)
item2 = Item("libreta", 4600, 8)
item3 = Item("pila AA", 800, 4)

pedido1 = Pedido("Compras clases")

pedido1.agregar_item(item1)
pedido1.agregar_item(item2)
pedido1.agregar_item(item3)
print("--------------------------------")
pedido1.calcular_total()

print("\n\t==== Ejercicio 4: Sensor ====")

km_hora = Sensor("km/h")

km_hora.agregar_valor(56)
km_hora.agregar_valor(30)
km_hora.agregar_valor(89)
km_hora.agregar_valor(12)

print(km_hora.minimo())
print(km_hora.maximo())
print(km_hora.promedio())

print("\n\t==== Ejercicio 5: Pelicula y Catalogo ====")

peli1 = Pelicula("Akira", "ciencia ficcion", 1988)
peli2 = Pelicula("Robot carnival", "ciencia ficcion", 1987)
peli3 = Pelicula("Atlantis", "aventura", 2001)
peli4 = Pelicula("Perfect blue", "misterio", 1997)

catalogo = Catalogo("Animacion")

catalogo.agregar_pelicula(peli1)
catalogo.agregar_pelicula(peli2)
catalogo.agregar_pelicula(peli3)
catalogo.agregar_pelicula(peli4)

catalogo.filtrar_por_genero("ciencia ficcion")
print("--------------------------------")
catalogo.buscar_por_titulo(peli1)
print("--------------------------------")
catalogo.listar_peliculas()

print("\n\t==== Ejercicio 6: Usuario y Auth ====")

user1 = Usuario('alondra','123qwe')
user2 = Usuario('rovin','psw000')
user3 = Usuario('foster','123123')
user4 = Usuario('marisol','asdfgh')

data = Auth()

data.login(user1,'qwertyu')
print("--------------------------------")
data.registrar_usuario(user1)
data.registrar_usuario(user2)
data.registrar_usuario(user3)
data.registrar_usuario(user4)
print("--------------------------------")
data.login(user1,'123qwe')
print("--------------------------------")
data.login(user2,'asdasd')
print("--------------------------------")
data.login(user4,'asdfgh')


print("\n\t==== Ejercicio 7: Contacto y Agenda ====")

contacto1 = Contacto("Alondra Gonzalez", 66857743, "alondra@correo.cl")
contacto2 = Contacto("Rovin Gatica", 23564478, "rovin@correo.cl")
contacto3 = Contacto("Diego Foster",88659301,"diego@correo.cl")

personal = Agenda("personal")

personal.agregar_contacto(contacto1)
personal.agregar_contacto(contacto2)
personal.agregar_contacto(contacto3)
print("--------------------------------")
personal.buscar_contacto(contacto2)
print("--------------------------------")
personal.eliminar_contacto(contacto1)
print("--------------------------------")
personal.listar_contactos()

print("\n\t==== Ejercicio 8: Mesa y Restaurante ====")

mesa1 = Mesa(1,4)
mesa2 = Mesa(2,8)
mesa3 = Mesa(3,6)
mesa4 = Mesa(4,2)

restaurante = Restaurante("Donde Pilon")

restaurante.agregar_mesa(mesa1)
restaurante.agregar_mesa(mesa2)
restaurante.agregar_mesa(mesa3)
restaurante.agregar_mesa(mesa4)
print("--------------------------------")
restaurante.reservar_mesa(mesa2,10)
restaurante.reservar_mesa(mesa2,8)

restaurante.reservar_mesa(mesa4,1) 
restaurante.reservar_mesa(mesa2,10)
restaurante.reservar_mesa(mesa1,3)
print("--------------------------------")
restaurante.liberar_mesa(mesa2)
print("--------------------------------")
restaurante.mostrar_mesas()

print("\n\t==== Ejercicio 9: Carrito y Producto ====")

arroz = Producto('arroz', 1200)
harina = Producto('harina', 950)
aceite = Producto('aceite', 1700)
leche = Producto('leche', 990)
fideos = Producto('fideos', 850)

super = Carrito()
super.agregar_producto(arroz, 4)
super.agregar_producto(harina, 3)
super.agregar_producto(aceite, 3)
super.agregar_producto(leche, 12)
super.agregar_producto(fideos, 5)
print("--------------------------------")
super.calcular_total()
print("--------------------------------")
super.aplicar_descuento(15, aceite)
super.aplicar_descuento(20, leche)
print("--------------------------------")
super. calcular_total()

print("\n\t==== Ejercicio 10: Estudiante y Nota ====\n")

nota1 = Nota("matematica", 5.5)
nota2 = Nota("lenguaje",4.3)
nota3 = Nota("historia", 3.9)
nota4 = Nota("quimica", 6.8)

estudiante = Estudiante("alondra")

estudiante.agregar_nota(nota1)
estudiante.agregar_nota(nota2)
estudiante.agregar_nota(nota3)
estudiante.agregar_nota(nota4)
print("--------------------------------")
estudiante.mostrar_calificaciones()
print("--------------------------------")
estudiante.calcular_promedio()

print("\n\t==== Ejercicio 11: Empleado y Empresa ====\n")

empleado1 = Empleado("alondra", 222000)
empleado2 = Empleado("marisol", 100500)
empleado3 = Empleado("rovin", 500500)
empleado4 = Empleado("foster", 300500)

empresa = Empresa("Minimarket")

empresa.contratar(empleado1)
empresa.contratar(empleado2)
empresa.contratar(empleado3)
empresa.contratar(empleado4)
print("--------------------------------")
empresa.listar_empleados()
print("--------------------------------")
empresa.calcular_sueldos()

print("\n\t==== Ejercicio 12: Cuenta y Banco ====")

cuenta1 = Cuenta('alondra', 850000)
cuenta2 = Cuenta('marisol', 2540000)
cuenta3 = Cuenta('rovin', 1405800)
cuenta4 = Cuenta('foster', 832000)

banco = Banco()

banco.ver_cuentas()
print("--------------------------------")
banco.abrir_cuenta(cuenta1)
banco.abrir_cuenta(cuenta2)
banco.abrir_cuenta(cuenta3)
banco.abrir_cuenta(cuenta4)
print("--------------------------------")
banco.transferir(cuenta2, cuenta1,250000)
print("--------------------------------")
banco.buscar_cuenta(cuenta3)
print("--------------------------------")
banco.ver_cuentas()


# print("\n\t==== Ejercicio 13: Mascota y Veterinaria ====")

# print("\n\t==== Ejercicio 14: Examen y Pregunta ====")
