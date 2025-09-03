#Ejercicio1

from ejercicio1.Clases.Libro_Biblioteca import Libro

libro1 = Libro("La casa de los espíritus", "Isabel Allende", 4)
libro2 = Libro("Los detectives salvajes", "Roberto Bolaño", 2)
libro3 = Libro("Desolación", "Gabriela Mistral", 6)

from ejercicio1.Clases.Libro_Biblioteca import Biblioteca

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

#Listado de libros

print("Listado de libros en la biblioteca:")
biblioteca.mostrar_libros()

#Préstamo de libros
biblioteca.prestar_libro("La casa de los espíritus")
biblioteca.mostrar_libros()

#Devolución de libros
biblioteca.devolver_libro("La casa de los espíritus")
biblioteca.mostrar_libros()

#Libro no encontrado
biblioteca.prestar_libro("Papelucho")


#------------------------------------------------------------#

#Ejercicio2

from ejercicio2.Alumno_Curso import Alumno

alumno1 = Alumno("Jairo Castillo")
alumno2 = Alumno("Nicole Zuñiga")
alumno3 = Alumno("Marco Rucal")


from ejercicio2.Alumno_Curso import Curso

curso = Curso("Programación Orientada a Objetos")
curso.inscribir_alumno(alumno1)
curso.inscribir_alumno(alumno2)
curso.inscribir_alumno(alumno3)

#Lista alumnos
print("Alumnos inscritos en el curso:")
curso.listar_alumnos()

#Remover un alumno
curso.remover_alumno(alumno2)
print("Alumnos inscritos en el curso después de remover a Nicole Zuñiga:")
curso.listar_alumnos()

#Inscribir un nuevo alumno
alumno4 = Alumno("Gonzalo Silva")
curso.inscribir_alumno(alumno4)
print("Alumnos inscritos en el curso después de inscribir a Gonzalo Silva:")
curso.listar_alumnos()



#------------------------------------------------------------#
# Ejercicio 3

from ejercicio3.Pedido_Item import Item, Pedido

#Creación de Ítems
print("Creando los ítems...")
item1 = Item(nombre="Manzana", precio=1200, cantidad=2)  
item2 = Item(nombre="Pan", precio=2000, cantidad=2)   
item3 = Item(nombre="Leche", precio=950, cantidad=3)   

#Creación del Pedido
mi_pedido = Pedido()

#Agrega los ítems al pedido
print("Agregando ítems al pedido...")
mi_pedido.agregar_item(item1)
mi_pedido.agregar_item(item2)
mi_pedido.agregar_item(item3)


#Subtotal() de un ítem individualmente
print(f"Calculando subtotal de '{item1.nombre}': ${item1.subtotal()}")
print(f"Calculando subtotal de '{item2.nombre}': ${item2.subtotal()}")
print(f"Calculando subtotal de '{item3.nombre}': ${item3.subtotal()}")  

# El total de todo el pedido
total_pedido = mi_pedido.calcular_total()
print(f"Total del pedido: ${total_pedido}")



#------------------------------------------------------------#

# #Ejercicio 4

from ejercicio4.Sensor_Mediciones import Sensor

# --- Creación del Sensor ---
# Sensor para medir la temperatura en Puente Alto.
sensor_puente_alto = Sensor(nombre="Temperatura Ambiental - Puente Alto")
print(f"Sensor '{sensor_puente_alto.nombre}' creado exitosamente.")

# --- Registro de Mediciones ---

print("\nRegistrando mediciones del día...")
sensor_puente_alto.registrar_medicion(12.5)
sensor_puente_alto.registrar_medicion(18.2)
sensor_puente_alto.registrar_medicion(21.8)
sensor_puente_alto.registrar_medicion(17.6) 
sensor_puente_alto.registrar_medicion(14.1) 

# Mostramos todas las mediciones registradas.
print(f"Mediciones registradas: {sensor_puente_alto.mediciones}")

# --- Cálculos ---
# Usamos los métodos de la clase para obtener y mostrar las estadísticas.
print("\nCalculando reporte meteorológico...")
promedio_dia = sensor_puente_alto.obtener_promedio()
maxima_dia = sensor_puente_alto.obtener_maximo()
minima_dia = sensor_puente_alto.obtener_minimo()

# --- Impresión del Reporte ---
print(f"\n--- 🌡️ Reporte del Día: {sensor_puente_alto.nombre} ---")
print(f"  - Temperatura Promedio: {promedio_dia:.1f}°C") # Usamos :.1f para 1 decimal
print(f"  - Temperatura Máxima: {maxima_dia}°C")
print(f"  - Temperatura Mínima: {minima_dia}°C")
print("-------------------------------------------------")



#------------------------------------------------------------#

# #Ejercicio 5

from ejercicio5.Pelicula_Catalogo import Pelicula, Catalogo

# --- 1. Creación del Catálogo ---
mi_catalogo = Catalogo()
print("Catálogo de películas creado.")

# --- 2. Creación y adición de Películas ---

print("Agregando películas al catálogo...")
mi_catalogo.agregar_pelicula(Pelicula("Machuca", "Drama", 2004))
mi_catalogo.agregar_pelicula(Pelicula("No", "Drama", 2012))
mi_catalogo.agregar_pelicula(Pelicula("Una Mujer Fantástica", "Drama", 2017))
mi_catalogo.agregar_pelicula(Pelicula("El Club", "Drama", 2015))
mi_catalogo.agregar_pelicula(Pelicula("Tony Manero", "Crimen", 2008))
mi_catalogo.agregar_pelicula(Pelicula("31 minutos, la película", "Animación", 2008))

# --- 3. Lista de todas las películas ---
print("--- 🎬 Listado Completo del Catálogo ---")
mi_catalogo.listar_todas()

# --- 4. Filtrar películas por género ---
print("--- 🎭 Filtrando por género: 'Drama' ---")
peliculas_drama = mi_catalogo.filtrar_por_genero("Drama")
for pelicula in peliculas_drama:
    print(f"  - {pelicula.titulo} ({pelicula.año})")

# --- 5. Buscar una película por título ---
print("--- 🔍 Buscando una película específica ---")

pelicula_encontrada = mi_catalogo.buscar_por_titulo("Machuca")
if pelicula_encontrada:
    print(f"¡Encontrada! -> Título: {pelicula_encontrada.titulo}, Género: {pelicula_encontrada.genero}, Año: {pelicula_encontrada.año}")
else:
    print("La película 'Machuca' no se encontró.")

# Caso 2: La película NO existe
pelicula_no_encontrada = mi_catalogo.buscar_por_titulo("Matrix")
if pelicula_no_encontrada:
    print(f"¡Encontrada! -> {pelicula_no_encontrada.titulo}")
else:
    print("La película 'Matrix' no se encontró.")

#------------------------------------------------------------#


# Ejercicio 6


from ejercicio6.Usuario_AutenticacionSimple import Usuario, Autentificacion 

# --- 1. Creación del Sistema de Autenticación ---
sistema_auth = Autentificacion()
print("Sistema de autenticación iniciado.")

# --- 2. Registro de Usuarios ---
print("Registrando nuevos usuarios...")
sistema_auth.registrar_usuario("j.castillo", "clave123")
sistema_auth.registrar_usuario("m.rucal", "seguridad_plus")
print("Usuarios 'j.castillo' y 'm.rucal' registrados.")

# --- 3. Pruebas de Login ---
print("--- Iniciando pruebas de login ---")

# Caso 1: Login Exitoso
print("Intentando login con 'j.castillo' y contraseña correcta...")
login_exitoso = sistema_auth.login("j.castillo", "clave123")
if login_exitoso:
    print("✅ ¡Login exitoso! Bienvenido, j.castillo.")
else:
    print("❌ Error: Usuario o contraseña incorrectos.")

# Caso 2: Login Fallido (Contraseña incorrecta)
print("\nIntentando login con 'm.rucal' y contraseña incorrecta...")
login_fallido = sistema_auth.login("m.rucal", "123456")
if login_fallido:
    print("✅ ¡Login exitoso! Bienvenido, m.rucal.")
else:
    print("❌ Error: Usuario o contraseña incorrectos.")

# Caso 3: Login Fallido (Usuario no existe)
print("Intentando login con usuario que no existe...")
login_inexistente = sistema_auth.login("a.garcia", "superclave")
if login_inexistente:
    print("✅ ¡Login exitoso! Bienvenido, a.garcia.")
else:
    print("❌ Error: Usuario o contraseña incorrectos.")



#------------------------------------------------------------#


# # Ejercicio 7

from ejercicio7.Agenda_Contacto import Contacto, Agenda

# --- 1. Creación de la Agenda y los Contactos ---
mi_agenda = Agenda()
print("Agenda personal creada.")

# Creamos algunos objetos Contacto
contacto1 = Contacto("Violeta Castillo", "+56912345678", "violeta.castillo@gmail.com")
contacto2 = Contacto("Vania Gómez", "+56987654321", "vania.gomez@gmail.com")
contacto3 = Contacto("Sergio Soto", "+56955554444", "sergio.soto@gmail.com")

# --- 2. Agregamos los contactos a la agenda ---
print("\nAgregando contactos...")
mi_agenda.agregar_contacto(contacto1)
mi_agenda.agregar_contacto(contacto2)
mi_agenda.agregar_contacto(contacto3)

# --- 3. Listamos todos los contactos ---
print("--- 📖 Mis Contactos ---")

lista_de_contactos = mi_agenda.listar_contactos()
for c in lista_de_contactos:
    print(f"  - Nombre: {c.nombre}, Teléfono: {c.telefono}, Correo: {c.correo}")
print("-------------------------")

# --- 4. Buscamos un contacto específico ---
print("\nBuscando a 'Vania Gómez'...")
contacto_buscado = mi_agenda.buscar_contacto("Vania Gómez")
if contacto_buscado:
    print(f"✔️ Contacto encontrado: {contacto_buscado.nombre} - {contacto_buscado.telefono} - {contacto_buscado.correo}")
else:
    print("❌ No se encontró el contacto.")

# --- 5. Eliminamos un contacto ---
print("\nEliminando a 'Sergio Soto'...")
eliminacion_exitosa = mi_agenda.eliminar_contacto("Sergio Soto")
if eliminacion_exitosa:
    print("✔️ Contacto eliminado correctamente.")
else:
    print("❌ No se pudo eliminar el contacto (no encontrado).")
    

# --- 6. Lista de contactos nuevamente para ver el cambio ---
print("--- 📖 Mis Contactos (Actualizado) ---")
lista_actualizada = mi_agenda.listar_contactos()
for c in lista_actualizada:
    print(f"  - Nombre: {c.nombre}, Teléfono: {c.telefono}, Correo: {c.correo}")
print("------------------------------------")


#------------------------------------------------------------#
#Ejercicio 8

from ejercicio8.Restaurante_Mesa_Reserva import Mesa, Restaurante

# --- 1. Creación del Restaurante y las Mesas ---
restaurante_Nani = Restaurante()
print("Restaurante 'El Sabor de la nani' ha abierto.")

# Las mesas al restaurante
restaurante_Nani.agregar_mesa(Mesa(numero=1, capacidad=4))
restaurante_Nani.agregar_mesa(Mesa(numero=2, capacidad=2))
restaurante_Nani.agregar_mesa(Mesa(numero=3, capacidad=6))
restaurante_Nani.agregar_mesa(Mesa(numero=4, capacidad=4))
print("Se han agregado 4 mesas al restaurante.")

# --- 2. Estado inicial de las mesas ---
print("--- Estado Inicial de las Mesas ---")
restaurante_Nani.mostrar_estado_mesas()
print("-----------------------------------")

# --- 3. Reserva ---
print("Un cliente quiere reservar la mesa 3...")
reserva_exitosa = restaurante_Nani.reservar_mesa(3)
if reserva_exitosa:
    print("✔️ Mesa 3 reservada exitosamente.")
else:
    print("❌ No se pudo reservar la mesa 3 (puede que no exista o ya esté ocupada).")

# --- 4. Estado después de la reserva ---
print("--- Estado Actualizado de las Mesas ---")
restaurante_Nani.mostrar_estado_mesas()
print("-------------------------------------")

# --- 5. Si se intenta reservar una mesa ya ocupada ---
print("Otro cliente intenta reservar la misma mesa 3...")
reserva_fallida = restaurante_Nani.reservar_mesa(3)
if reserva_fallida:
    print("✔️ Mesa 3 reservada exitosamente.")
else:
    print("❌ No se pudo reservar la mesa 3 (ya está ocupada).")

# --- 6. Se libera la mesa ---
print("El cliente de la mesa 3 se va. Liberando mesa...")
liberacion_exitosa = restaurante_Nani.liberar_mesa(3)
if liberacion_exitosa:
    print("✔️ Mesa 3 liberada.")
else:
    print("❌ No se pudo liberar la mesa 3.")

# --- 7. El Estado final ---
print("--- Estado Final de las Mesas ---")
restaurante_Nani.mostrar_estado_mesas()
print("---------------------------------")


#------------------------------------------------------------#


# #Ejercicio 9

from ejercicio9.CarritoConDescuento import Producto, Carrito

# --- 1. Creación de los Productos y el Carrito ---

p1 = Producto("Leche Entera", 950)
p2 = Producto("Pan Hallulla", 2200) # Precio por Kg
p3 = Producto("Queso Gauda", 12990) # Precio por Kg
p4 = Producto("Bebida Coca-Cola 1.5L", 1500)

print("Productos seleccionados: Leche Entera, Pan Hallulla, Queso Gauda, Bebida Coca-Cola 1.5L.")

# Creación de carrito de compras
mi_carrito = Carrito()
print("Carrito de compras listo.")

# --- 2. Productos al carrito ---
print("Agregando productos al carrito...")
mi_carrito.agregar_producto(p1, 2) # 2 cajas de Leche
mi_carrito.agregar_producto(p2, 0.5) # Medio kilo de Pan
mi_carrito.agregar_producto(p3, 0.25) # 250 gr de Queso
mi_carrito.agregar_producto(p4, 3) # 3 Bebidas

# --- 3. Se Calcula el total sin descuento ---
total_sin_descuento = mi_carrito.calcular_total()
print(f"🛒 Total sin descuento: ${total_sin_descuento:,.0f}")

# --- 4. Se Aplica un descuento ---
porcentaje_descuento = 15 # Un 15% de descuento
print(f"Aplicando un {porcentaje_descuento}% de descuento...")
total_con_descuento = mi_carrito.aplicar_descuento(porcentaje_descuento)

# --- 5. Se muestra el total final ---
print(f"💰 Total final a pagar: ${total_con_descuento:,.0f}")



#------------------------------------------------------------#

# #Ejercicio 10
from ejercicio10.Estudiante_Nota import Nota, Estudiante

# --- 1. Creación de los Estudiantes ---

estudiante1 = Estudiante("Jairo Castillo")
estudiante2 = Estudiante("Nicole Zuñiga")
estudiante3 = Estudiante("Javiera Espindola")
estudiante4 = Estudiante("Gonzalo Silva")

print("Se han inscrito 4 nuevos estudiantes.")

# --- 2. Las notas para cada Estudiante ---
print("Registrando calificaciones...")

# Notas para Jairo Castillo
estudiante1.agregar_nota(Nota("Programación", 6.5))
estudiante1.agregar_nota(Nota("Bases de Datos", 5.8))
estudiante1.agregar_nota(Nota("Redes", 6.1))

# Notas para Nicole Zuñiga
estudiante2.agregar_nota(Nota("Programación", 7.0))
estudiante2.agregar_nota(Nota("Bases de Datos", 6.5))
estudiante2.agregar_nota(Nota("Redes", 6.8))

# Notas para Javiera Espindola
estudiante3.agregar_nota(Nota("Programación", 5.5))
estudiante3.agregar_nota(Nota("Bases de Datos", 4.8))
estudiante3.agregar_nota(Nota("Redes", 5.1))

# Notas para Gonzalo Silva
estudiante4.agregar_nota(Nota("Programación", 4.2))
estudiante4.agregar_nota(Nota("Bases de Datos", 5.0))
estudiante4.agregar_nota(Nota("Redes", 4.5))

# --- 3. Reporte de un estudiante ---
print("--- 🎓 Reporte Académico Individual ---")
print(f"Estudiante: {estudiante2.nombre}")
estudiante2.mostrar_calificaciones()
promedio_nicole = estudiante2.calcular_promedio()
print(f"Promedio Final: {promedio_nicole:.1f}")
print("---------------------------------------")

# --- 4. Resumen de todo el curso ---
print("--- 📋 Resumen de Promedios del Curso ---")
lista_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4]
for est in lista_estudiantes:
    promedio = est.calcular_promedio()
    print(f"  - {est.nombre}: Promedio {promedio:.1f}")
print("-----------------------------------------")



#------------------------------------------------------------#

# #Ejercicio 11

from ejercicio11.Empleado_Empresa import Empleado, Empresa

# --- 1. Creación de la Empresa ---
empresa_viopallets = Empresa()
print("🏢 Empresa 'Viopallets' ha sido creada.")

# --- 2. Creación y Contratación de Empleados ---
print("...Contratando personal...")

emp1 = Empleado("Alfredo Carrasco", 1200000)
emp2 = Empleado("Jorge Castillo", 950000)
emp3 = Empleado("Alexis Fuentes", 880000)
emp4 = Empleado("Rodolfo Gonzalez", 1150000)
emp5 = Empleado("Rodrigo Villegas", 920000)

# Método de la empresa para contratarlos
empresa_viopallets.contratar_empleado(emp1)
empresa_viopallets.contratar_empleado(emp2)
empresa_viopallets.contratar_empleado(emp3)
empresa_viopallets.contratar_empleado(emp4)
empresa_viopallets.contratar_empleado(emp5)

# Lista de todos los empleados de la empresa ---
print("--- 👥 Listado de Empleados: Viopallets ---")
empresa_viopallets.listar_empleados()
print("------------------------------------------")

# --- 4. Gasto total en sueldos ---
gasto_total = empresa_viopallets.calcular_gasto_total()
print(f"💸 Gasto total mensual en sueldos: ${gasto_total:,.0f}")


#------------------------------------------------------------#


# #Ejercicio 12

from ejercicio12.Banco_Cuentas import Banco, Cuenta

# --- 1. Creación del Banco y las Cuentas ---
banco_santander = Banco()
print("🏦 Banco Santander ha iniciado operaciones.")

# Las cuentas
cuenta_jairo = Cuenta(titular="Jairo Castillo", saldo=500000)
cuenta_mercadopago = Cuenta(titular="Cuenta de ahorro para la vivienda", saldo=0)

# El banco abre las cuentas
banco_santander.abrir_cuenta(cuenta_jairo)
banco_santander.abrir_cuenta(cuenta_mercadopago)
print("Cuentas abiertas para 'Jairo Castillo' con 'Cuenta de ahorro para la vivienda'.")

# --- 2. El estado inicial de las cuentas ---
print("--- 📊 Estado Inicial de Cuentas ---")
banco_santander.mostrar_estado_cuentas()
print("------------------------------------")

# --- 3. Realizamos una transferencia ---
monto_transferencia = 25000
print(f"Realizando transferencia de ${monto_transferencia} desde 'Jairo Castillo' a 'Cuenta de ahorro para la vivienda'...")

transferencia_exitosa = banco_santander.transferir_dinero(
    de_titular="Jairo Castillo",
    a_titular="Cuenta de ahorro para la vivienda",
    monto=monto_transferencia
)

if transferencia_exitosa:
    print("✔️ Transferencia realizada con éxito.")
else:
    print("❌ Error: No se pudo realizar la transferencia. Verifique los datos o el saldo.")

# --- 4. Mostramos el estado final de las cuentas ---
print("--- 📊 Estado Final de Cuentas ---")
banco_santander.mostrar_estado_cuentas()
print("---------------------------------")

#------------------------------------------------------------#

# # Ejercicio 13

from ejercicio13.Mascotas_Veterinaria import Mascota, Veterinaria

# --- 1. Veterinaria ---
veterinaria_patitas = Veterinaria()
print("🐾 Veterinaria 'Patitas Sanas' ha abierto.")

# Las mascotas que llegarán a la consulta
mascota1 = Mascota(nombre="Dora", especie="Perro", edad=5)
mascota2 = Mascota(nombre="Mishi", especie="Gato", edad=2)
mascota3 = Mascota(nombre="Rocky", especie="Perro", edad=8)
mascota4 = Mascota(nombre="Piolín", especie="Canario", edad=1)

# --- 2. Registro de las mascotas en la veterinaria ---
print("Registrando mascotas...")
veterinaria_patitas.registrar_mascota(mascota1)
veterinaria_patitas.registrar_mascota(mascota2)
veterinaria_patitas.registrar_mascota(mascota3)
veterinaria_patitas.registrar_mascota(mascota4)

# --- 3. Lista todas las mascotas registradas ---
print("--- 📋 Fichas de Pacientes ---")
veterinaria_patitas.listar_mascotas()
print("-----------------------------")

# --- 4. Busqueda de una mascota por su nombre ---
print("Buscando a la mascota 'Mishi'...")
mascota_encontrada = veterinaria_patitas.buscar_mascota("Mishi")
if mascota_encontrada:
    print(f"✔️ Ficha encontrada: {mascota_encontrada.nombre}, {mascota_encontrada.especie} de {mascota_encontrada.edad} años.")
else:
    print("❌ No se encontró la ficha de la mascota.")

# --- 5. Edad promedio de los pacientes ---
edad_promedio = veterinaria_patitas.calcular_edad_promedio()
print(f"\n📊 La edad promedio de las mascotas es de {edad_promedio:.1f} años.")



#------------------------------------------------------------#
#Ejercicio 14

from ejercicio14.Examen_Preguntas import Examen,Pregunta

# --- 1. Creación del Examen y las Preguntas ---
examen_final = Examen()
print("📝 Examen Inacap.")

# Creamos las preguntas que irán en el examen
p1 = Pregunta("¿Cuál es la capital de Chile?", "Santiago")
p2 = Pregunta("¿Qué es un 'string' en programación?", "Una secuencia de caracteres")
p3 = Pregunta("¿En que año Chile gano su primera copa america?", "2015")
p4 = Pregunta("¿Qué método se usa para añadir un elemento a una lista en Python?", "append()")

#2
examen_final.agregar_pregunta(p1)
examen_final.agregar_pregunta(p2)
examen_final.agregar_pregunta(p3)
examen_final.agregar_pregunta(p4)

# --- 3. Listamos todas las preguntas del examen ---
print("--- ✍️  Preguntas del Examen ---")
examen_final.listar_preguntas()
print("--------------------------------------")

# --- 4. Contamos el total de preguntas ---
total_de_preguntas = examen_final.contar_preguntas()
print(f"📊 El examen contiene un total de {total_de_preguntas} preguntas.")
