from math import trunc

class Carrito:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto, cantidad):
        self.carrito.append({"producto": producto, "cantidad": cantidad}) # <-- almacenamos el objeto producto para usarlo despues
        print(f"\nAgregaste {producto.nombre}({cantidad}) al carrito")

    def calcular_total(self):
        if self.carrito:
            print("\n--- Carrito de compras ---\n")
            subtotal = []
            for item in self.carrito:
                # "sacar" al objeto producto del diccionario para poder usarlo como objeto de mejor manera
                producto = item['producto'] 
                print(f"* {producto.nombre:10} x{item['cantidad']:2} ${trunc(producto.precio):5} = ${trunc(producto.precio * item['cantidad'])}")
                # Almacenamos el precio total de los productos
                subtotal.append(trunc(producto.precio * item['cantidad'])) 
            print(f"\nTotal: ${sum(subtotal)}")
        else:
            print("\nNo tienes productos en el carrito")

    def aplicar_descuento(self, descuento, producto):
        if self.carrito:
            desc = descuento / 100
            producto.precio *= desc
            print(f"\n-{descuento}% aplicado a {producto.nombre}, nuevo precio ${trunc(producto.precio)}")
        else:
            print("\nNo tienes productos en el carrito")




