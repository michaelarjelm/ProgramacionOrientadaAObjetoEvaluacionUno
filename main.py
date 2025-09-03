

# # ejercicio uno libro y blibliioteca 

# from ejercicio1.clases.libro import Libro
# from ejercicio1.clases.biblioteca import Biblioteca
# # esta es lka lista de libros 
# biblio = Biblioteca()
# libro1 = Libro(" Un secreto en mi colegio ", " Angelica Dossetti ", 4)
# libro2 = Libro(" No toques a mi madre ", " Herve Mestron ", 3)

# # Aqui se agregan los libros 

# biblio.agregar(libro1)
# biblio.agregar(libro2)

# # accion de prestar o devolver 

# biblio.prestar("Un secreto en mi Colegio")
# biblio.devolver("No toques a mi Madre ")

# biblio.listar()



#ejercicio dos Alumno y Clase 

# from para llamar a las clases 
# from ejercicio2.clases.Alumno import Alumno
# from ejercicio2.clases.Curso import Curso
# # nombre curso y nombre alumnos 
# curso = Curso("analistas,programadores Inacap")
# alumno1 = Alumno("Carlos blanco")
# alumno2 = Alumno("Edgar ojeda")

# curso.inscribir(alumno1)
# curso.inscribir(alumno2)
# curso.remover("Carlos")  

# print("Alumnos inscritos:", curso.listar())



#ejercicio numero tres >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#crear clase item y pedido

from ejercicio3.clases.item import Item
from ejercicio3.clases.pedido import Pedido

if __name__ == "__main__":
    pedido = Pedido()

    #  Aqui Agregamos productos
    pedido.agregar_item(Item("Pan", 1500, 2))
    pedido.agregar_item(Item("Bebida", 1200, 3))
    pedido.agregar_item(Item("Queso Gauda", 2500, 1))

    # aqui mostramos el detalle del pedido
    pedido.mostrar_detalle()
