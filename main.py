#ejercicio 1
from ejercicio_1.libro_biblioteca import Libro, Biblioteca 

def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Salir")

def agregar_libro_interactivo(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    try:
        cantidad = int(input("Ingrese la cantidad de copias: "))
        if cantidad <= 0:
            print("La cantidad de copias debe ser mayor a 0.")
            return
    except ValueError:
        print("Entrada inválida para la cantidad de copias.")
        return

    libro = Libro(titulo, autor, cantidad)
    biblioteca.agregar_libro(libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

def prestar_libro_interactivo(biblioteca):

    #ejercicio 2 curso y alumno

    from ejercicio_2.curso_alumno import Alumno, Curso

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Crear un curso")
    print("2. Gestionar un curso")
    print("3. Ver todos los cursos")
    print("4. Salir")

def crear_curso(cursos):
    nombre_curso = input("Ingrese el nombre del curso: ")
    nuevo_curso = cursos(nombre_curso)
    cursos.append(nuevo_curso)
    print(f"Curso {nombre_curso} creado.")

def seleccionar_curso(cursos):
    if not cursos:
        print("No hay cursos creados ahora, crea un curso primero para que hagas clases mi loco.")
        return None

    print("\n--- Cursos disponibles ---")
    for i, curso in enumerate(cursos):
        print(f"{i + 1}. {curso.nombre}")

    while True:
        try:
            opcion = int(input("Seleccione el número del curso: "))
            if 1 <= opcion <= len(cursos):
                return cursos[opcion - 1]
            else:
                print("Opción inválida, selecciona un numero de la listo mi herman@ lista.")
        except ValueError:
            print("Entrada inválida mi loco, Por favor, ingrese un número otra vez.")

def gestionar_curso(curso):
    while True:
        print(f"\n--- Gestionando el curso {curso.nombre} ---")
        print("1. Inscribir alumno")
        print("2. Remover alumno")
        print("3. Listar alumnos")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            alumno = Alumno(nombre_alumno)
            curso.inscribir_alumno(alumno)
        elif opcion == "2":
            nombre_alumno = input("Ingrese el nombre del alumno a remover: ")
            alumno = Alumno(nombre_alumno)
            curso.remover_alumno(alumno)
        elif opcion == "3":
            curso.listar_alumnos()
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opcion invalida. Por favor, seleccione una opción del menu.")

def main():
    cursos = []  # Lista para guardar los cursos hechos :o

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_curso(cursos)
        elif opcion == "2":
            curso_seleccionado = seleccionar_curso(cursos)
            if curso_seleccionado:
                gestionar_curso(curso_seleccionado)
        elif opcion == "3":
            if not cursos:
                print("No hay cursos creados.")
            else:
                print("\n--- Cursos creados ---")
                for curso in cursos:
                    print(curso)
        elif opcion == "4":
            print("Hasta la otra pa")
            break
        else:
            print("Opcion invalida prueba otra vez.")

if __name__ == "__main__":
    main()

#ejercicio 3 

from ejercicio_3.pedido_item import Ítem, Pedido  # Importa las clases

def mostrar_menu():
    print("\n--- Menú del Pedido ---")
    print("1. Agregar ítem")
    print("2. Mostrar pedido")
    print("3. Calcular total")
    print("4. Salir")

def agregar_item_interactivo(pedido):
    nombre = input("Ingrese el nombre del ítem: ")
    try:
        precio = float(input("Ingrese el precio del ítem: "))
        cantidad = int(input("Ingrese la cantidad: "))
        if precio < 0 or cantidad < 0:
            print("El precio y la cantidad deben ser mayores o iguales a cero")
            return
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos")
        return

    item = Ítem(nombre, precio, cantidad)
    pedido.agregar_item(item)

def mostrar_pedido_interactivo(pedido):
    print(pedido)  

def calcular_total_interactivo(pedido):
    total = pedido.calcular_total()
    print(f"El total del pedido es: ${total:.2f}")

def main():
    pedido = Pedido()  # Crea una instancia de la clase

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_item_interactivo(pedido)
        elif opcion == '2':
            mostrar_pedido_interactivo(pedido)
        elif opcion == '3':
            calcular_total_interactivo(pedido)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()

#ejercicio 4

from ejercicio_4. sensor  import Sensor
def main():
    # Sensor de temperatura exterior (continuación del ejemplo original)
    sensor_temperatura = Sensor("Temperatura Exterior")
    sensor_temperatura.registrar_valor(22.5)
    sensor_temperatura.registrar_valor(23.1)
    sensor_temperatura.registrar_valor(21.9)
    sensor_temperatura.registrar_valor(24.0)
    sensor_temperatura.registrar_valor(22.8)

    print(sensor_temperatura)
    print(f"Promedio de temperatura: {sensor_temperatura.obtener_promedio():.2f}°C")
    print(f"Temperatura máxima: {sensor_temperatura.obtener_maximo()}°C")
    print(f"Temperatura mínima: {sensor_temperatura.obtener_minimo()}°C")

#ejercicio 5 
from ejercicio_5.pelicula_catalogo import Pelicula, Catalogo  

def mostrar_menu():
    print("\n--- Menú del Catálogo ---")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Buscar por título")
    print("4. Filtrar por género")
    print("5. Salir")

def agregar_pelicula_interactivo(catalogo):
    titulo = input("Ingrese el título de la película: ")
    genero = input("Ingrese el género de la película: ")
    try:
        anio = int(input("Ingrese el año de la pelicula: "))
    except ValueError:
        print("Entrada invalida para el año debe ser un numero entero.")
        return

    pelicula = Pelicula(titulo, genero, anio)
    catalogo.agregar_pelicula(pelicula)

def listar_peliculas_interactivo(catalogo):
    catalogo.listar_peliculas()

def buscar_por_titulo_interactivo(catalogo):
    titulo = input("Ingrese el título a buscar: ")
    catalogo.buscar_por_titulo(titulo)

def filtrar_por_genero_interactivo(catalogo):
    genero = input("Ingrese el género a filtrar: ")
    catalogo.filtrar_por_genero(genero)

def main():
    catalogo = Catalogo()  # Crea una instancia de la clase Catalogo

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pelicula_interactivo(catalogo)
        elif opcion == "2":
            listar_peliculas_interactivo(catalogo)
        elif opcion == "3":
            buscar_por_titulo_interactivo(catalogo)
        elif opcion == "4":
            filtrar_por_genero_interactivo(catalogo)
        elif opcion == "5":
            print("hasta el otro año mano")
            break
        else:
            print("opcion mala, pone una opcion del menu")

if __name__ == "__main__":
    main()

#ejerciocio 6

from ejercicio_6.usuario_autenticacion_simple import Auth 

def mostrar_menu():
    print("\n--- Menú de Autenticación ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def registrar_usuario_interactivo(auth):
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if auth.registrar(nombre_usuario, contrasena):
        print("registro exitoso.")
    else:
        print("error en el registro.")

def iniciar_sesion_interactivo(auth):
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if auth.login(nombre_usuario, contrasena):
        print("Sesión iniciada")
        # Aquí podrías agregar lógica para la sesión activa, como mostrar un menú de usuario, etc.
    else:
        print("error al iniciar sesión.")

def main():
    auth = Auth()  # Crea una instancia de la clase Auth

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario_interactivo(auth)
        elif opcion == "2":
            iniciar_sesion_interactivo(auth)
        elif opcion == "3":
            print("hasta la otra papito")
            break
        else:
            print("opción inválida, seleccione una opción del menú.")

if __name__ == "__main__":
    main()

#ejercicio 7

from ejercicio_7. agenda import Contacto, Agenda  
def mostrar_menu():
    print("\n--- Menú de Agenda ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar contactos")
    print("5. Salir")

def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    contacto = Contacto(nombre, telefono, correo)
    agenda.agregar_contacto(contacto)

def buscar_contacto(agenda):
    nombre = input("Nombre del contacto a buscar: ")
    contacto = agenda.buscar_contacto(nombre)
    if contacto:
        print(contacto)
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Nombre del contacto a eliminar: ")
    agenda.eliminar_contacto(nombre)

def listar_contactos(agenda):
    agenda.listar_contactos()

def main():
    mi_agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_contacto(mi_agenda)
        elif opcion == "2":
            buscar_contacto(mi_agenda)
        elif opcion == "3":
            eliminar_contacto(mi_agenda)
        elif opcion == "4":
            listar_contactos(mi_agenda)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()

#ejercicio 8

from ejercicio_8.mesa_restaurante import Mesa, Restaurante
def mostrar_menu():
    print("\n--- Menú del Restaurante ---")
    print("1. Agregar Mesa")
    print("2. Reservar Mesa")
    print("3. Liberar Mesa")
    print("4. Mostrar Estado de Mesas")
    print("5. Salir")

def agregar_mesa_interactiva(restaurante):
    try:
        numero = int(input("Ingrese el número de la mesa: "))
        capacidad = int(input("Ingrese la capacidad de la mesa: "))
        nueva_mesa = Mesa(numero, capacidad)
        restaurante.agregar_mesa(nueva_mesa)
        print(f"Mesa {numero} agregada.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")

def reservar_mesa_interactiva(restaurante):
    try:
        numero = int(input("Ingrese el número de la mesa a reservar: "))
        print(restaurante.reservar_mesa(numero))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

def liberar_mesa_interactiva(restaurante):
    try:
        numero = int(input("Ingrese el número de la mesa a liberar: "))
        print(restaurante.liberar_mesa(numero))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

def main():
    mi_restaurante = Restaurante()  # Crear una instancia del restaurante

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_mesa_interactiva(mi_restaurante)
        elif opcion == "2":
            reservar_mesa_interactiva(mi_restaurante)
        elif opcion == "3":
            liberar_mesa_interactiva(mi_restaurante)
        elif opcion == "4":
            mi_restaurante.mostrar_estado_mesas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()

#ejercicio 9

from ejercicio_9.carrito import Producto, Carrito  

# Ejemplo de uso
if __name__ == "__main__":
    #Crear productos
    producto1 = Producto("Camiseta", 20)
    producto2 = Producto("Pantalón", 50)
    producto3 = Producto("Zapatos", 80)

    #Crear carrito
    mi_carrito = Carrito()

    # Agregar productos al carrito
    mi_carrito.agregar_producto(producto1, 2)  # 2 camisetas
    mi_carrito.agregar_producto(producto2, 1)  # 1 pantalón
    mi_carrito.agregar_producto(producto3, 1)  # 1 par de zapatos

    # Calcular el total sin descuento
    total_sin_descuento = mi_carrito.calcular_total()
    print(f"Total sin descuento: {total_sin_descuento}")

    # Aplicar un descuento del 10%
    total_con_descuento = mi_carrito.aplicar_descuento(10)
    print(f"Total con descuento (10%): {total_con_descuento}")

#ejercicio_10
from ejercicio_10.nota import Nota, Estudiante

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar estudiante")
    print("2. Agregar nota a estudiante")
    print("3. Mostrar calificaciones de estudiante")
    print("4. Calcular promedio de estudiante")
    print("5. Salir")

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiante = Estudiante(nombre)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado.")

def agregar_nota(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    for estudiante in estudiantes:
        if estudiante.nombre == nombre_estudiante:
            asignatura = input("Ingrese la asignatura: ")
            try:
                calificacion = float(input("Ingrese la calificación: "))
                nota = Nota(asignatura, calificacion)
                estudiante.agregar_nota(nota)
                print("Nota agregada.")
            except ValueError:
                print("Error: Ingrese una calificación válida (número).")
            return
    print("Estudiante no encontrado.")

def mostrar_calificaciones(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    for estudiante in estudiantes:
        if estudiante.nombre == nombre_estudiante:
            estudiante.mostrar_calificaciones()
            return
    print("Estudiante no encontrado.")

def calcular_promedio(estudiantes):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    for estudiante in estudiantes:
        if estudiante.nombre == nombre_estudiante:
            promedio = estudiante.calcular_promedio()
            print(f"Promedio de {estudiante.nombre}: {promedio}")
            return
    print("Estudiante no encontrado.")

def main():
    estudiantes = []  # Lista para almacenar los estudiantes

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            agregar_nota(estudiantes)
        elif opcion == "3":
            mostrar_calificaciones(estudiantes)
        elif opcion == "4":
            calcular_promedio(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#ejercicio 11

from ejercicio_11.empleado_empresa import Empleado, Empresa 

def main():
    # Crear empleados
    empleado1 = Empleado("ruth", 3000)
    empleado2 = Empleado("Samuel", 4000)
    empleado3 = Empleado("Bastian", 3500)

    # Crear empresa
    empresa1 = Empresa("mi empresa")

    #Contratar empleados
    empresa1.contratar_empleado(empleado1)
    empresa1.contratar_empleado(empleado2)
    empresa1.contratar_empleado(empleado3)

    # Listar empleados
    print("\nListado de empleados:")
    empresa1.listar_empleados()

    #Calcular y mostrar el gasto total en sueldos
    gasto_total = empresa1.calcular_gasto_total_sueldos()
    print(f"\nGasto total en sueldos: {gasto_total}")

if __name__ == "__main__":
    main()

#ejercicio 12

# main.py
from ejercicio_12.banco_y_cuentas import Banco 

def main():
    # Crear un banco
    mi_banco = Banco()

    # Abrir cuentas
    mi_banco.abrir_cuenta("Juan Pérez", 1000)
    mi_banco.abrir_cuenta("María García", 500)
    mi_banco.abrir_cuenta("Pedro López")  #Cuenta con saldo inicial 0

    #Mostrar estado inicial de las cuentas
    print("\nEstado inicial de las cuentas:")
    mi_banco.mostrar_estado_cuentas()

    #Realizar algunas transacciones
    mi_banco.transferir("Juan Pérez", "María García", 200)
    mi_banco.transferir("María García", "Pedro López", 100)
    mi_banco.transferir("Ana Sánchez", "Juan Pérez", 50)  #Intentar transferir de una cuenta que no existe

    #Intentar retirar
    cuenta_juan = mi_banco.buscar_cuenta("Juan Pérez")
    if cuenta_juan:
        cuenta_juan.retirar(1500)  #Intenta retirar más de lo que tiene

    #Mostrar estado final de las cuentas
    print("\nEstado final de las cuentas:")
    mi_banco.mostrar_estado_cuentas()

if __name__ == "__main__":
    main()

#ejercicio 13
from ejercicio_13.veterinaria import Mascota, Veterinaria

if __name__ == "__main__":
    #Creamos una instancia de la veterinaria
    mi_veterinaria = Veterinaria()

    #Creamos algunas mascotas de ejemplo
    mascota1 = Mascota("Firulais", "Perro", 5)
    mascota2 = Mascota("Michi", "Gato", 3)
    mascota3 = Mascota("Rocky", "Perro", 7)
    mascota4 = Mascota("Loro", "Ave", 2)

    #Registramos las mascotas en la veterinaria
    mi_veterinaria.registrar_mascota(mascota1)
    mi_veterinaria.registrar_mascota(mascota2)
    mi_veterinaria.registrar_mascota(mascota3)
    mi_veterinaria.registrar_mascota(mascota4)

    #Listamos todas las mascotas registradas
    mi_veterinaria.listar_mascotas()

    #Buscamos una mascota por nombre
    nombre_a_buscar = "Michi"
    mi_veterinaria.buscar_mascota(nombre_a_buscar)

    #Intentamos buscar una mascota que no existe
    nombre_a_buscar_inexistente = "Wally"
    mi_veterinaria.buscar_mascota(nombre_a_buscar_inexistente)

    #Calculamos y mostramos la edad promedio de las mascotas
    mi_veterinaria.calcular_edad_promedio()

#ejercicio 14

from ejercicio_14.pregunta import Pregunta, Examen  # Importa las clases desde el archivo pregunta.py

def evaluar_examen(examen):
    """
    Evalúa las respuestas de un estudiante.

    Args:
        examen (Examen): El objeto Examen a evaluar.
    """
    if not examen.preguntas:
        print("El examen está vacío. No se puede evaluar.")
        return

    puntaje_total = 0
    for i, pregunta in enumerate(examen.preguntas):
        respuesta_estudiante = input(f"Pregunta {i + 1}: {pregunta.enunciado}\nTu respuesta: ")
        if respuesta_estudiante.strip().lower() == pregunta.respuesta_correcta.strip().lower():
            print("¡Correcto!")
            puntaje_total += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta.respuesta_correcta}")

    print(f"\nTu puntaje total es: {puntaje_total} de {examen.contar_preguntas()}")

def guardar_examen(examen, nombre_archivo="examen.txt"):
    """
    Guarda el examen en un archivo de texto.

    Args:
        examen (Examen): El objeto Examen a guardar.
        nombre_archivo (str): El nombre del archivo donde guardar el examen.
    """
    try:
        with open(nombre_archivo, "w") as archivo:
            for pregunta in examen.preguntas:
                archivo.write(f"{pregunta.enunciado}|{pregunta.respuesta_correcta}\n")
        print(f"Examen guardado en '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al guardar el examen: {e}")

def cargar_examen(nombre_archivo="examen.txt"):
    """
    Carga un examen desde un archivo de texto.

    Args:
        nombre_archivo (str): El nombre del archivo del que cargar el examen.

    Returns:
        Examen: El objeto Examen cargado, o None si hubo un error.
    """
    examen = Examen()
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                enunciado, respuesta_correcta = linea.strip().split("|")
                pregunta = Pregunta(enunciado, respuesta_correcta)
                examen.agregar_pregunta(pregunta)
        print(f"Examen cargado desde '{nombre_archivo}'")
        return examen
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al cargar el examen: {e}")
        return None


if __name__ == "__main__":
    #Crear un examen
    mi_examen = Examen()

    #Crear preguntas (puedes mover esto a una función para organizar mejor)
    pregunta1 = Pregunta("¿Cuál es la capital de Francia?", "París")
    pregunta2 = Pregunta("¿Cuál es el resultado de 2 + 2?", "4")
    pregunta3 = Pregunta("¿En qué año se descubrió América?", "1492")

    #Agregar preguntas al examen
    mi_examen.agregar_pregunta(pregunta1)
    mi_examen.agregar_pregunta(pregunta2)
    mi_examen.agregar_pregunta(pregunta3)

    #Listar las preguntas
    mi_examen.listar_preguntas()

    #Evaluar el examen
    evaluar_examen(mi_examen)

    #Guardar el examen
    guardar_examen(mi_examen, "mi_examen.txt")

    #Cargar un examen (prueba)
    examen_cargado = cargar_examen("mi_examen.txt")
    if examen_cargado:
        print("\nExamen cargado:")
        examen_cargado.listar_preguntas()
        evaluar_examen(examen_cargado)  #Evaluar el examen cargado
