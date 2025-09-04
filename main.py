
#Ejercicio1

from Ejercicio1.LibroBiblioteca import Libro
from Ejercicio1.LibroBiblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    libro1 = Libro("El escarabajo de oro", "Allan Poe", 2)
    libro2 = Libro("Terapia para llevar", "Ana Perez", 1)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.mostrar_libros()

    biblioteca.prestar_libro("El escarabajo de oro")
    biblioteca.mostrar_libros()

    biblioteca.devolver_libro("El escarabajo de oro")
    biblioteca.mostrar_libros()


#Ejercicio2

from Ejercicio2.AlumnoCurso import Alumno
from Ejercicio2.AlumnoCurso import Curso

def main():
    curso = Curso("Matematica")

    alumno1 = Alumno("Angela")
    alumno2 = Alumno("Isabella")
    alumno3 = Alumno("Romane")

    curso.inscribir_alumno(alumno1)
    curso.inscribir_alumno(alumno2)
    curso.inscribir_alumno(alumno3)

    curso.listar_alumnos()

    curso.remover_alumno("Isabella")
    curso.listar_alumnos()

#Ejercicio3

from Ejercicio3.PedidoItem import Item
from Ejercicio3.PedidoItem import Pedido

def main():
    pedido = Pedido()

    # Crear ítem
    item1 = Item("Notebook", 350.000, 1)
    item2 = Item("Celular", 150.000, 2)
    item3 = Item("Pantalla", 80.000, 4)

    # Agregar ítem al pedido
    pedido.agregar_item(item1)
    pedido.agregar_item(item2)
    pedido.agregar_item(item3)

    # Mostrar el pedido y total
    pedido.mostrar_pedido()

#Ejercicio4

from Ejercicio4.SensorMediciones import Sensor 

def main():
    sensor = Sensor("Temperatura")
    sensor.registrar(10)
    sensor.registrar(20)
    sensor.registrar(15)

    print("Promedio:", sensor.promedio())
    print("Máximo:", sensor.maximo())
    print("Mínimo:", sensor.minimo())


#Ejercicio5   

from Ejercicio5.PeliculaCatalogo import Pelicula
from Ejercicio5.PeliculaCatalogo import Catalogo

def main():
    catalogo = Catalogo()

    # Agregar películas
    catalogo.agregar(Pelicula("Inception", "Ciencia Ficción", 2010))
    catalogo.agregar(Pelicula("Titanic", "Romance", 1997))
    catalogo.agregar(Pelicula("Avatar", "Ciencia Ficción", 2009))
    catalogo.agregar(Pelicula("Gladiator", "Acción", 2000))

    # Listar todas
    print("Todas las películas:")
    for p in catalogo.listar():
        print(p)

    # Buscar por título
    print("Buscar 'Titanic':")
    peli = catalogo.buscar_por_titulo("Titanic")
    if peli:
        print(peli)
    else:
        print("No encontrada")

    # Filtrar por género
    print("Películas de Ciencia Ficción:")
    for p in catalogo.filtrar_por_genero("Ciencia Ficción"):
        print(p) 


#Ejercicio6

from Ejercicio6.UsuarioAutenticacion import Auth

def main():
    sistema = Auth()

    # Registrar usuarios
    print("Registrar usuarios:")
    print(sistema.registrar("Angela", "0123"))
    print(sistema.registrar("Romane", "efgh")) 
    print(sistema.registrar("Angela", "otro"))  

    print("Intentos de login:")
    print(sistema.login("Romane", "0123")) 
    print(sistema.login("Angela", "efgh"))  
    print(sistema.login("Angela", "*****"))   
    print(sistema.login("Esperanza", "0123"))


#Ejercicio7

from Ejercicio7.Agenda_y_contacto import Agenda

def main():
    agenda = Agenda()

    # Agregar contactos
    agenda.agregar("Andres", "123456789", "andres@mail.com")
    agenda.agregar("Camila", "987654321", "camila@mail.com")
    agenda.agregar("Pedro", "555666777", "pedro@mail.com")

    # Listar contactos
    print("📒 Contactos en la agenda:")
    for c in agenda.listar():
        print(c)

    # Buscar contacto
    print("Buscar Camila:")
    contacto = agenda.buscar("Camila")
    if contacto:
        print(contacto)
    else:
        print("No encontrado")

    # Eliminar contacto
    print("Eliminando Andres")
    agenda.eliminar("Andres")

    # Listar de nuevo
    print("Agenda actualizada:")
    for c in agenda.listar():
        print(c)    

#Ejercicio8

from Ejercicio8.RestauranteMesa import Restaurante

def main():
    rest = Restaurante("Esperanza de Sabor")

    # Agregar mesas
    rest.agregar_mesa(1, 2)
    rest.agregar_mesa(2, 4)
    rest.agregar_mesa(3, 6)

    # Mostrar estado inicial
    print("Estado inicial de las mesas:")
    for estado in rest.mostrar_estado():
        print(estado)

    # Reservar mesas
    print("Reservando mesa 2")
    print("Reserva exitosa" if rest.reservar_mesa(2) else "No disponible")

    # Mostrar estado después de reservar
    print("Estado después de la reserva:")
    for estado in rest.mostrar_estado():
        print(estado)

    # Liberar mesa
    print("Liberando mesa 2")
    print("Liberada con éxito" if rest.liberar_mesa(2) else "No se pudo liberar")

    # Estado final
    print("Estado final:")
    for estado in rest.mostrar_estado():
        print(estado)

#Ejercicio9

from Ejercicio9.CarritoDescuento import Producto
from Ejercicio9.CarritoDescuento import Carrito

def main():
    # Crear productos
    p1 = Producto("Manzana", 0.5)
    p2 = Producto("Pan", 1.2)
    p3 = Producto("Leche", 0.9)

    # Crear carrito
    carrito = Carrito()

    # Agregar productos
    carrito.agregar(p1, 4)   # 4 manzanas
    carrito.agregar(p2, 2)   # 2 panes
    carrito.agregar(p3, 1)   # 1 leche

    # Mostrar carrito
    print("Carrito de compras:")
    for item in carrito.mostrar():
        print(item)

    # Totales
    print(f"\nTotal sin descuento: ${carrito.total():.2f}")
    print(f"Total con 10% de descuento: ${carrito.total_con_descuento(10):.2f}")


#Ejercicio 10

from Ejercicio10.EstudianteNota import Estudiante

def main():
    estudiante = Estudiante("Paola")

    # Agregar notas
    estudiante.agregar_nota("Matemáticas", 4.5)
    estudiante.agregar_nota("Historia", 7.0)
    estudiante.agregar_nota("Ciencias", 6.5)

    # Mostrar todas las calificaciones
    print(f"Notas de {estudiante.nombre}:")
    for nota in estudiante.mostrar_notas():
        print(nota)

    # Promedio
    print(f"Promedio: {estudiante.promedio():.2f}")

#Ejercicio11

from Ejercicio11.EmpleadoEmpresa import Empresa

def main():
    empresa = Empresa("Tech Solutions")

    # Contratar empleados
    empresa.contratar("Ana", 2500)
    empresa.contratar("Luis", 3000)
    empresa.contratar("María", 2800)

    # Listar empleados
    print(f"Empleados en {empresa.nombre}:")
    for e in empresa.listar_empleados():
        print(e)

    # Gasto total en sueldo
    print(f"Gasto total en sueldos: ${empresa.gasto_total():.2f}")


#Ejercicio 12

from Ejercicio12.BancoCuenta import Banco

def main():
    banco = Banco("Banco Central")

    # Abrir cuentas
    banco.abrir_cuenta("Ana", 1.000)
    banco.abrir_cuenta("Luis", 5.000)
    banco.abrir_cuenta("María", 4.000)

    # Mostrar estado inicial
    print(f"Estado inicial de {banco.nombre}:")
    for estado in banco.mostrar_estado():
        print(estado)

    # Transferir dinero
    print("Transfiriendo $1.000 de Ana a Luis")
    if banco.transferir("Ana", "Luis", 10.000):
        print("Transferencia exitosa")
    else:
        print("Error en la transferencia")

    # Estado después de transferir
    print(f"final de {banco.nombre}:")
    for estado in banco.mostrar_estado():
        print(estado)



