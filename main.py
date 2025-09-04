#Ejercicio1 Clases(Libro y Biblioteca)

from ejercicio1.Clases.libro import Libro
from ejercicio1.Clases.biblioteca import Biblioteca

def main():

    libro1 = Libro("Las aventuras de Alicia en el país de las maravillas", "Lewis Carroll", 1)
    libro2 = Libro("El maravilloso mago de Oz", "L. Frank Bauméry", 2)


    biblioteca = Biblioteca()


    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
     


    biblioteca.mostrar_libros()


    biblioteca.prestar_libro("Las aventuras de Alicia en el país de las maravillas")


    biblioteca.devolver_libro("Las aventuras de Alicia en el país de las maravillas")


    biblioteca.mostrar_libros()

if __name__ == "__main__":
    main() 



#Ejercicio2 Clases(Alumno,Curso)

from ejercicio2.Clases.alumno import Alumno
from ejercicio2.Clases.curso import Curso


from ejercicio2.Clases.alumno import Alumno
from ejercicio2.Clases.curso import Curso

def main():
    curso1 = Curso("Python")

    alumno1 = Alumno("Diego")
    alumno2 = Alumno("Pedro")
    alumno3 = Alumno("Juan")
    alumno4 = Alumno("Carlos")

    curso1.inscribir(alumno1)
    curso1.inscribir(alumno2)
    curso1.inscribir(alumno3)
    curso1.inscribir(alumno4)

    curso1.listar_alumnos()

    curso1.remover("Pedro")
    curso1.remover("Carlos")

    curso1.listar_alumnos()

if __name__ == "__main__":
    main()
   


#Ejercicio3 Clases(Item,Pedido)

from ejercicio3.Clases.item import Item
from ejercicio3.Clases.pedido import Pedido

def main():

    item1 = Item("Polera",20,12)
    item2 = Item("Pantalon",15,10)
    item3 = Item("Zapatillas",10,50)

    pedido1 = Pedido()

    pedido1.agregar_item(item1)
    pedido1.agregar_item(item2)
    pedido1.agregar_item(item3)
    
    
    pedido1.mostrar_pedido()

    pedido1.calcular_total()

    pedido1.mostrar_pedido()
    
    
if __name__ == "__main__":
    main()  


#Ejercicio4 Clases(Sensor)
from ejercicio4.Clases.sensor import Sensor

def main():
    
    print("Sensor de sismos")
   

    sensor1 = Sensor("Sensor de sismos")


    sensor1.registrar(4.5)
    sensor1.registrar(6.2)
    sensor1.registrar(5.1)

   
    print("\nAquí esta el promedio el maximo y el minimo:")
   
    sensor1.mostrar_info()

if __name__ == "__main__":
      main()




#Ejercicio5 Clases(Pelicula,Catalogo)
from ejercicio5.Clases.pelicula import Pelicula
from ejercicio5.Clases.catalogo import Catalogo


def main():
    catalogo = Catalogo()

    peli1 = Pelicula("Como entrenar a tu dragon","fantasía y aventura",2010)
    peli2 = Pelicula("Titanes del Pacifico","Ciencia ficción",2010)
    peli3 = Pelicula("Cars","Inantil/Comedia",2006)

    catalogo.agregar(peli1)
    catalogo.agregar(peli2)
    catalogo.agregar(peli3)


    catalogo.listar()


    print("Búsqueda por título:")
    peli = catalogo.buscar_por_titulo("Como entrenar a tu dragon")
    if peli:
     print("Encontrada:", peli)
    else:
            print("No encontrada.")


    print("\nPelículas de Ciencia ficción:")
    for p in catalogo.filtrar_por_genero("Ciencia ficción"):
        print(peli)


if __name__ == "__main__":
    main()


#Ejercicio6 Clases(Usuario,Auth)
from ejercicio6.Clases.usuario import Usuario
from ejercicio6.Clases.auth import Auth

def main():

    auth = Auth()

    auth.registrar("Edgar", "123456")
    auth.registrar("Juan", "1234")

    auth.login("Edgar","123456")
    auth.login("Juan","1234")
    
    for u in auth.usuarios:
        print(u)  


if __name__ == "__main__":
    main()




#Ejercicio 7 Clases(Contacto-Agenda)
from ejercicio7.Clases.contacto import Contacto
from ejercicio7.Clases.agenda import Agenda

def main():

    agenda = Agenda()

    contacto1 = Contacto("Juan",91812818,"Juancorreo@correo.com")
    contacto2 = Contacto("Pedro",917237137,"Pedrocorreo@correo.com")



  
    agenda.agregar(contacto1)
    agenda.agregar(contacto2)


    agenda.buscar(contacto1)

    agenda.eliminar("Juan")


    agenda.listar()

if __name__ == "__main__":     
        main()



#Ejercicio8 Clases(Mesa-Restaurante)
from ejercicio8.Clases.mesa import Mesa
from ejercicio8.Clases.restaurante import Restaurante

def main():
    mesa1 = Mesa(1, 5)
    mesa2 = Mesa(2, 3)
    mesa3 = Mesa(3, 4)

    restaurante = Restaurante()
    restaurante.agregar_mesas(mesa1)
    restaurante.agregar_mesas(mesa2)
    restaurante.agregar_mesas(mesa3)

    restaurante.reservar(1)
    restaurante.reservar(2)
    restaurante.reservar(3)
    
    restaurante.mostrar_estado()

    restaurante.liberar(2)
    restaurante.liberar(3)

if __name__ == "__main__":
    main()


#Ejercicio9 Clases(Carrito-Producto)
from ejercicio9.Clases.carrito import Carrito
from ejercicio9.Clases.producto import Producto


def main():
    
    
    carrito = Carrito()


    producto1 = Producto("Camisa", 100,2)
    producto2= Producto("Pantalón", 150,4)


    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    total = carrito.calcular_total()
    
    print (f"Total a pagar: ${total}")

    
    conDescuento =  carrito.descuento(15)
    
    print(f"Total con descuento:${conDescuento} ")

if __name__ == "__main__":
    main()


#Ejercicio 10 Clases(Nota,Estudiante)

from ejercicio10.Clases.nota import Nota
from ejercicio10.Clases.estudiante import Estudiante

def main(): 


    estudiante = Estudiante("Edgar")
    nota1 = Nota ("Programación Orientada a Objetos",4.0)
    nota2 = Nota("Base de datos",4.5)

    estudiante.agregar_notas(nota1)
    estudiante.agregar_notas(nota2)


    notas = estudiante.mostrar_calificaciones()

    promedio = estudiante.calcular_promedio()
    print(f"El promedio de {estudiante.nombre} es: {promedio:.1f}")




if __name__ == "__main__":
    main()



#Ejercicio 11 Clases(Empleado,Empresa)

from ejercicio11.Clases.empleado import Empleado
from ejercicio11.Clases.empresa import Empresa


def main():

    empresa = Empresa()

    empleado1 = Empleado("juan",1121)
    empleado2 = Empleado("Pedro",200)


   
    empresa.contratar_empleado(empleado1)
    empresa.contratar_empleado(empleado2)


    empresa.listar_empleados()


    print (f"El gasto toal de la empresa es:${empresa.gasto_total()}")


if __name__ == "__main__":
    main()


#Ejercicio12 Clases(Cuenta-Banco)


from ejercicio12.Clases.cuenta import Cuenta
from ejercicio12.Clases.banco import Banco


def main():

    banco = Banco("Banco estado")
    cuenta1 = Cuenta("Diego", 1000)      
    cuenta2 = Cuenta("Juan", 500)


    banco.abrir_cuenta(cuenta1)
    banco.abrir_cuenta(cuenta2)

    banco.transferir(cuenta1, cuenta2, 200)

    banco.mostrar_estado()

if __name__ == "__main__":
    main()

    

#Ejercicio 13 Clases(Mascota-Veterinaria)

from ejercicio13.Clases.mascota import Mascota
from ejercicio13.Clases.veterinaria import Veterinaria

def main(): 
    
    veterinaria = Veterinaria("Veterinaria")

    mascota1 = Mascota("Firulo","perro",8) 
    mascota2 = Mascota("Cachupin","perro",2)


    veterinaria.registra_mascota(mascota1)
    veterinaria.registra_mascota(mascota2)

    veterinaria.listar_mascotas()

    veterinaria.calcular_Edad()

if __name__ == "__main__":
    main()



#Ejercicio14 Clases(Examen-Pregunta)

from ejercicio14.Clases.examen import Examen
from ejercicio14.Clases.pregunta import Pregunta

def main():


    examen = Examen("Examen")

    pregunta1 = Pregunta("¿Que es python?","Un lenguaje de programación")
    pregunta2 = Pregunta("¿Que es POO?","Programación Orientada a Objetos")


    examen.agregar_pregunta(pregunta1)
    examen.agregar_pregunta(pregunta2)


    examen.listar_preguntas()


    examen.total_preguntas()



if __name__ == "__main__":
    main()







    



